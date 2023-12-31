export default function createInt8TypedArray(length, position, value) {
  const ab = new ArrayBuffer(length);
  const view = new DataView(ab);
  if (position > length) throw Error('Position outside range');
  view.setInt8(position, value);
  return view;
}
