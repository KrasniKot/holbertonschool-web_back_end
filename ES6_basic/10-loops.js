export default function appendToEachArrayValue(array, appendString) {
  const aray = [];
  for (const value of array) {
    aray.push(appendString + value);
  }

  return aray;
}
