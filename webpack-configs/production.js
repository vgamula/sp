const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
require('babel-polyfill');

const sourcePath = './client/';
const sourceFilePath = './client/index';
const destinationPath = './server/static/dist/';
const statsFile = destinationPath + 'stats.json';
const vendorManifestFile = destinationPath + 'vendor-manifest.json';

const manifest = require('.' + vendorManifestFile);

module.exports = {
    context: path.resolve(__dirname, '..'),

    entry: {
        main: [
            'babel-polyfill',
            sourceFilePath,
        ],
    },

    output: {
        path: path.resolve('.' + destinationPath),
        filename: '[name]-[hash].js',
    },

    plugins: [
        new webpack.NoErrorsPlugin(),
        new webpack.optimize.DedupePlugin(),
        new BundleTracker({filename: statsFile}),
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: JSON.stringify('production')
            }
        }),
        new webpack.optimize.OccurenceOrderPlugin(),
        new webpack.optimize.UglifyJsPlugin(),
        new webpack.DllReferencePlugin({
            name: 'vendor',
            context: sourcePath,
            manifest: manifest,
        }),
        new webpack.optimize.AggressiveMergingPlugin(),
    ],

    module: {
        loaders: [
            {test: /\.js$/, exclude: /node_modules/, loaders: ['babel', 'eslint-loader']},
        ]
    },

    resolve: {
        root: [
            sourcePath,
        ],
        modulesDirectories: ['node_modules'],
        extensions: ['', '.js']
    },

    resolveLoader: {
        modulesDirectories: ['node_modules'],
        moduleTemplates: ['*-loader', '*'],
        extensions: ['', '.js']
    },
};
