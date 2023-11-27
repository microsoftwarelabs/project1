// JavaScript Anti-Keylogger Script 
(function () { 
// String to simulate typing 
var stringToType = createRandomString(5); 
// 5 is the length of the random string 
 
// Function to create a random string 
 function createRandomString(length) { 
var result = ''; 
 var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'; 
for (var i = 0; i < length; i++) { 
 result += characters.charAt(Math.floor(Math.random() * characters.length)); 
 } 
return result; 
 } 

 // Function to simulate typing 
 function simulateTyping(text) { 
 for (var i = 0; i < text.length; i++) { 
 var character = text.charAt(i); 
 var keyEvent = new KeyboardEvent('keydown', { key: character }); 
 document.dispatchEvent(keyEvent); 
 setTimeout(function () { 
 var keyupEvent = new KeyboardEvent('keyup', { key: character }); 
 document.dispatchEvent(keyupEvent); 
 }, 100); 
 } 
 } 
 
 // Example usage: Simulate typing the word 'secret' inside the script 
 simulateTyping(stringToType); 
})();