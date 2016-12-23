/* eslint-disable */

const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const DashboardPlugin = require('webpack-dashboard/plugin');

const config = require('./development.js');

const compiler = webpack(config);
compiler.apply(new DashboardPlugin());

new WebpackDevServer(compiler, {
    publicPath: config.output.publicPath,
    hot: true,
    inline: true,
    historyApiFallback: true,
}).listen(3000, '0.0.0.0', (err) => {
    if (err) {
        console.log(err);
    }
    console.log('Listening at 0.0.0.0:3000');
});
