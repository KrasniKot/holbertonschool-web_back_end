export default function appendToEachArrayValue(array, appendString) {
  const aray = [];
  for (let value of array) {
    aray.push(appendString + value);
  }

  return aray;
}
