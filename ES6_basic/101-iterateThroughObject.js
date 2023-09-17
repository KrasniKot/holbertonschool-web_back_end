export default function iterateThroughObject(reportWithIterator) {
  let empray = "";

  for (let emp of reportWithIterator) {
    empray += emp;
    empray += " | ";
  }

  return empray.slice(0, -3);
}
