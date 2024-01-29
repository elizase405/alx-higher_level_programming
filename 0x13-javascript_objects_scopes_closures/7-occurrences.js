function nbOccurences (list, searchElement) {
  let count = 0;

  for (val of list) {
    if (val === searchElement) {
      count++;
    }
  }

  return count;
}

exports.nbOccurences = nbOccurences;
