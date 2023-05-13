const path = require('path')

// common used module rules
const moduleRules = {
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
};

module.exports = [
// App core  
    {
    entry: {
        core: './core/static/core/js/base.js',
    },
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'core', 'static', 'core', 'dist'), // <= diff output path
    },
    module: moduleRules,
    },

    // App info
    {
    entry: {
        info: './info/static/info/js/base.js',
    },
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'info', 'static', 'info', 'dist'), // <= diff output path
    },
    module: moduleRules,
    },
];
