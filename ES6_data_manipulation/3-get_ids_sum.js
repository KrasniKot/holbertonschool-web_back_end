export default function getStudentIdsSum(stnts) {
  return stnts.reduce((total, stnt) => total + stnt.id, 0);
}
