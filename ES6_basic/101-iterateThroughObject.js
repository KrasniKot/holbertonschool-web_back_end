export default function iterateThroughObject(reportWithIterator) {
  let empray = '';

  for (const emp of reportWithIterator) {
    empray += emp;
    empray += ' | ';
  }

  return empray.slice(0, -3);
}
