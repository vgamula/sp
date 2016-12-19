require('babel-polyfill')
import React from 'react'
import ReactDOM from 'react-dom'

import Application from 'app'


ReactDOM.render(<Application name="World"/>, document.getElementById('app'))


if (module.hot) {
    module.hot.accept(['./app', './index', 'app', 'index'], () => {
        const NextApp = require('./app').default  // eslint-disable-line
        ReactDOM.render(
            <NextApp name="World"/>,
            document.getElementById('app')
        )
    })
}
