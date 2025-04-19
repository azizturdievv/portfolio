import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";
import { collection, addDoc } from "@firebase/firestore";

const firebaseConfig = {    
    apiKey: "AIzaSyC7Ccv7Y2Dv62aoA3RjIEbd0ZZI5Ayzlg8",
    authDomain: "turdievuz-17cd5.firebaseapp.com",
    projectId: "turdievuz-17cd5",
    storageBucket: "turdievuz-17cd5.firebasestorage.app",
    messagingSenderId: "916504670816",
    appId: "1:916504670816:web:2383c665ddc3439a810905",

   
   
    // apiKey: "AIzaSyDJPq9a0YPoQYkpQ-Uaw7aXQRXzzqOKzFA",
    // authDomain: "web-kelas-tes.firebaseapp.com",
    // projectId: "web-kelas-tes",
    // storageBucket: "web-kelas-tes.appspot.com",
    // messagingSenderId: "890817433268",
    // appId: "1:890817433268:web:11e5258f8864a6174c11e1"
};

// Initialize with a unique name
const app = initializeApp(firebaseConfig, 'comments-app');
const db = getFirestore(app);
const storage = getStorage(app);

export { db, storage, collection, addDoc };