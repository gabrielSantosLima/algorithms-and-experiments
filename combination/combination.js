// ==== UTILS ====
function fat(n) {
  if (n === 2) {
    return 2;
  }
  return n * fat(n - 1);
}

function C(n, p) {
  if (n === p) return 1;
  return fat(n) / (fat(p) * fat(n - p));
}

// ==== MAIN ====

function combine22(group = []) {
  const totalSize = group.length;
  let combinations = [];
  for (let index = 0; index < totalSize - 1; index++) {
    for (let nextIndex = index + 1; nextIndex < totalSize; nextIndex++) {
      combinations.push([group[index], group[nextIndex]]);
    }
  }
  return combinations;
}

function combineNN(group = [], p) {
  const totalSize = group.length;
  let combinations = [];
  for (let index = 0; index <= totalSize - p; index++) {
    const subgroup = group.slice(index + 1, totalSize);
    const recursiveCombinations = combine(subgroup, p - 1);
    for (const recursiveCombination of recursiveCombinations) {
      combinations.push([group[index], ...recursiveCombination]);
    }
  }
  return combinations;
}

function combine(group = [], p) {
  if (p <= 0) return [];
  if (p === 1) return [...group];
  if (p === 2) return combine22(group);
  return combineNN(group, p);
}

module.exports = {
  C,
  combine,
};
