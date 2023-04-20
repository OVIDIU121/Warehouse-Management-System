class InventoryList extends React.Component {
    state = {
      inventories: [],
    };
  
    componentDidMount() {
      this.fetchInventories();
    }
  
    fetchInventories = () => {
      fetch("/api/inventory/")
        .then((res) => res.json())
        .then((data) => {
          const promises = data.map((inventory) => {
            const itemPromise = fetch(`/api/items/${inventory.item}/`).then((res) =>
              res.json()
            );
            const locationPromise = fetch(
              `/api/locations/${inventory.location}/`
            ).then((res) => res.json());
  
            return Promise.all([itemPromise, locationPromise]).then(
              ([itemData, locationData]) => ({
                ...inventory,
                itemName: itemData.name,
                locationName: locationData.name,
              })
            );
          });
  
          Promise.all(promises).then((inventories) =>
            this.setState({ inventories })
          );
        });
    };
  
    render() {
      const { inventories } = this.state;
  
      return (
 <div class="vh-100 d-flex justify-content-center align-items-center">
  <div class="container">
    <div class="row d-flex justify-content-center"></div>
        <h2 class="fw-bold mb-2 text-uppercase">
        Inventory List
        </h2>
          <table class="table table-striped table-hover" >
            <thead>
              <tr>
                <th>Location</th>
                <th>Item</th>
                <th>Quantity</th>
              </tr>
            </thead>
            <tbody>
              {inventories.map((inventory) => (
                <tr key={inventory.id}>
                  <td>{inventory.locationName}</td>
                  <td>{inventory.itemName}</td>
                  <td>{inventory.quantity}</td>
                </tr>
              ))}
            </tbody>
          </table>
     </div>
</div>
        
      );
    }
  }

  ReactDOM.render(<InventoryList />, document.getElementById("root"));