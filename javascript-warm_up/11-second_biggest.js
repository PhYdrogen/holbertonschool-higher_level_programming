#!/usr/bin/node
const argv = process.argv;
if ((argv.length === 2) || (argv[2] === '1' && argv.length < 3)) {
  console.log('0');
} else {
  const numbersList = argv.slice(2);
  numbersList.sort(function (a, b) { return a - b; });
  console.log(numbersList[numbersList.length - 2]);
}
