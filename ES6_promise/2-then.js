/* eslint-disable no-unused-vars */
export default function handleResponseFromAPI(promise) {
  console.log('Got a response from the API');
  return new Promise((resolve, reject) => {
    if (success) { resolve({ status: 200, body: 'success' }); } else { reject(new Error()); }
  });
}
/* eslint-enable no-unused-vars */
