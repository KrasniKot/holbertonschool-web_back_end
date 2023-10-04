import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()]).then([pres, ures]) => {
    console.log(results[0].body, results[1].firstName, results[1].lastName);
  }).catch((err) => { console.log('Signup system offline'); });
}
