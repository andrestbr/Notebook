var a = [1,2,3,4,5,6,7,8,9,10];

function mean(values) {
  var length = values.length;
  var sum = 0;

  for (var i = 0; i<length; i++){
    sum += values[i];
  }
  return (sum/length);
}