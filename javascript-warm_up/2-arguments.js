#!/usr/bin/node
const { argv } = require('node:process');

const nbArg = argv.length;
if (nbArg === 2) {
    console.log('No argument');
} else if (nbArg === 3){
    console.log('Argument found');
} else if (nbArg > 3) {
    console.log('Arguments found');
}