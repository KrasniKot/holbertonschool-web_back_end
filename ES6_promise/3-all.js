import { uploadPhoto, createUser } from './utils';

/* eslint-disable no-unused-vars */
export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()]).then((results) => {
    console.log(results[0].body, results[1].firstName, results[1].lastName);
  }).catch((err) => { console.log('Signup system offline'); });
}
/* eslint-enable no-unused-vars */
