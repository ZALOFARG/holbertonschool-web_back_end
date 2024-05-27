export default function cleanSet(set, startString) {
  let phrase = '';
  if (startString && typeof startString === 'string') {
    set.forEach((value) => {
      if (value.startsWith(startString)) {
        phrase += `${value.slice(startString.length)}-`;
      }
    });
    return phrase.slice(0, -1);
  }
  return phrase;
}
