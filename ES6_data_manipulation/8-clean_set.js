export default function cleanSet(set, startString) {
  let result = '';
  if (!startString || !startString.length) return result;
  for (const value of set) { if (value && value.startsWith(startString)) { result += `${value.slice(startString.length)}-`; } }
  return result.slice(0, result.length - 1);
}
