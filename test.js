const sdk = require('api')('@opensea/v1.0#bg4ikl1mk428b');

sdk['retrieving-asset-events']({
  collection_slug: 'akc',
  event_type: 'successful',
  'X-API-KEY': '5ca9ad56f654460c95f7c1aa25cbcd13'
})
  .then(res => console.log(res))
  .catch(err => console.error(err));