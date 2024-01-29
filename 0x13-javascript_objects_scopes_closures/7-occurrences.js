function nbOccurences (list, searchElement) {
  let count = 0;

  for (const val of list) {
    if (val === searchElement) {
      count++;
    }
  }

  return count;
}

exports.nbOccurences = nbOccurences;
