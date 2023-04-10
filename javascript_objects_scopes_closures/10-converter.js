#!/usr/bin/node
// Comprendre la closure c'est pas si simple
function converter (base) {
  function myConverter (num) {
    //console.log('my:' + num);
    return num.toString(base);
  }
  //console.log('conv: '+ base);
  return myConverter;
}
module.exports = { converter };