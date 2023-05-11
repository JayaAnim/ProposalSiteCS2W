const path = require('path')


module.exports = {
    entry: {
        core: './core/static/core/js/base.js',
        info: './info/static/info/js/base.js',
    },
    output: {
        filename: '[name]/bundle.js',
        path: path.resolve(__dirname, 'core', 'static', 'dist'),
    },
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader'],
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/i,
                type: 'asset/resource',
            },
        ],
    },
};

