function addInventoryItem(itemId, quantity, locationId) {
    const data = {
      quantity: quantity,
      item: itemId,      
      location: locationId,
    };
  
    fetch('/api/inventory/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log('Inventory item added successfully:', data);
    })
    .catch(error => {
      console.error('There was an error adding inventory item:', error);
    });
  }