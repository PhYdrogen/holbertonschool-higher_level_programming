#!/usr/bin/node

//const { read } = require("fs");

const fs = request('fs').promises;

async function readFile(file) {
    try {
        const data = await fs.readFile(file);
        console.log(data.toString());
    } catch (err) {
        console.log(err);
    }
}

readFile(process.argv[1])