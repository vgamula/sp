import React from 'react'
import { Test } from 'reloadable'

export default function Hello({ name }) {
    return (
        <div>
            Hey, {name}!
            <Test />
        </div>
    )
}
