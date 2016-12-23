/* eslint-disable */

const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const AnyBarWebpackPlugin = require('anybar-webpack');
require('babel-polyfill');

const projectPath = path.resolve(__dirname, '..');
const sourcePath = './client/';
const sourceFilePath = './client/index';
const destinationPath = './server/static/dist/';
const statsFile = destinationPath + 'stats.json';
const vendorManifestFile = destinationPath + 'vendor-manifest.json';
const publicPath = 'http://localhost:3000/static/dist/';

const manifest = require('.' + vendorManifestFile);


module.exports = {
    context: projectPath,

    entry: {
        main: [
            'babel-polyfill',
            'webpack-dev-server/client?http://localhost:3000',
            'webpack/hot/only-dev-server',
            sourceFilePath,
        ]
    },

    output: {
        path: path.join(projectPath, destinationPath),
        filename: '[name]-[hash].js',
        publicPath: publicPath,
    },

    plugins: [
        new webpack.NoErrorsPlugin(),
        new webpack.HotModuleReplacementPlugin(),
        new webpack.DllReferencePlugin({
            name: 'vendor',
            context: sourcePath,
            manifest: manifest,
        }),
        new BundleTracker({filename: statsFile}),
        new AnyBarWebpackPlugin(),
    ],

    module: {
        loaders: [
            {test: /\.js$/, exclude: /node_modules/, loaders: ['react-hot-loader/webpack', 'babel', 'eslint-loader']},
        ]
    },

    resolve: {
        root: [
            path.join(projectPath, sourcePath),
        ],
        modulesDirectories: ['node_modules'],
        extensions: ['', '.js']
    },

    resolveLoader: {
        modulesDirectories: ['node_modules'],
        moduleTemplates: ['*-loader', '*'],
        extensions: ['', '.js']
    },
    watch: true,
    devtool: 'source-map',
};
