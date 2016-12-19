const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
require('babel-polyfill');

const isProduction = process.env.NODE_ENV === 'production';
console.log(`Production mode - ${isProduction}`);

const projectPath = path.resolve(__dirname, '..');
const sourcePath = './client/';
const destinationPath = './server/static/dist/';
const statsFile = destinationPath + 'vendor-stats.json';
const publicPath = 'http://localhost:3000/static/dist/';

const config = {
    context: path.resolve(__dirname, '..'),

    entry: {
        vendor: [
            'babel-core/register',
            'babel-polyfill',
            'react',
            'react-dom',
        ]
    },

    output: {
        path: destinationPath,
        filename: '[name]-[hash].js',
        library: '[name]',
    },

    plugins: [
        new webpack.optimize.DedupePlugin(),
        new webpack.NoErrorsPlugin(),
        new webpack.optimize.DedupePlugin(),
        new BundleTracker({filename: statsFile}),
        new webpack.optimize.OccurenceOrderPlugin(),
        new webpack.DllPlugin({
            name: '[name]',
            path: path.join(destinationPath, '[name]-manifest.json'),
            context: sourcePath,
        })
    ],

    module: {
        loaders: [
            {test: /\.js$/, exclude: /node_modules/, loaders: ['babel', 'eslint-loader']},
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
    devtool: (isProduction ? 'eval' : 'source-map'),
};

if (isProduction) {
    config.plugins = config.plugins.concat([
        new webpack.optimize.UglifyJsPlugin(),
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: JSON.stringify('production')
            }
        }),
        new webpack.optimize.AggressiveMergingPlugin(),
    ])
} else {
    config.output.publicPath = publicPath;
}

module.exports = config;
