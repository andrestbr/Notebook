function mean(numbersForMean) {
  var length = numbersForMean.length;
  var sum = 0;

  for (var i = 0; i<length; i++){
    sum += numbersForMean[i];
  }
  return (sum/length);
}