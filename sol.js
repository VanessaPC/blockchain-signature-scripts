export const SOLConverstion = (hex: string) => {
  //const hex = '2606fd6eda22b6890d8fdb2722b9980b3f1a5e264196fa8c9e7102b5c70dfe8befd688d9175f55ee97b2a93cc55878f4cb639c96bb9360f11c679ba8468cd82e';

  const toBytes = Array.from(hex.match(/.{1,2}/g).map((b) => parseInt(b, 16)));
  return JSON.stringify(toBytes);
};

//example of return
// JSON Secret Key Array:
// [38,6,253,110,218,34,182,137,13,143,219,39,34,185,152,11,63,26,94,38,65,150,250,140,158,113,2,181,199,13,254,139,239,214,136,217,23,95,85,238,151,178,169,60,197,88,120,244,203,99,156,150,187,147,96,241,28,103,155,168,70,140,216,46]

// Copy the entire array (including brackets) and paste it into the private key field in Brave wallet.
