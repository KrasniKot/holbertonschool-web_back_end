export default function getStudentsByLocation(stnts, city) {
  return stnts.filter((stnt) => stnt.location === city);
}
