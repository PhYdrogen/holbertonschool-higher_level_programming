#!/usr/bin/node
function converter (base) {
  function myConverter (num) {
    return num.toString(base);
  }
  return myConverter;
}
module.exports = { converter };
