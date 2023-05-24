import json

# Open the JSON file and load its contents
with open('jobs.json', 'r') as file:
    jobs = json.load(file)

# Modify each job object by adding campaign parameters
for job in jobs:
    job['applicationURL'] += '?utm_source=job-board&utm_medium=website&utm_campaign=job-listing'

# Save the modified data back to the file
with open('jobs.json', 'w') as file:
    json.dump(jobs, file, indent=2)




    const filterLocationSelect = document.querySelector('#filter-location');

    filterLocationSelect.addEventListener('change', () => {
      const selectedLocation = filterLocationSelect.value;
      const selectedTag = document.querySelector('#filter-type').value;
      jobListings.forEach((listing) => {
        const tags = listing.querySelectorAll('.tag');
        const location = listing.querySelector('.location'); // Get the location element
        let showList = false;
        let showLocation = false;
        let showCategory = false;
        tags.forEach((tag) => {
          if (selectedTag === 'all' || tag.textContent.toLowerCase() === selectedTag) {
            showList = true;
          }
        });
        if (selectedLocation === 'all' || location.textContent.toLowerCase() === selectedLocation) {
          showLocation = true; // Check against the location element's text content
        }
        const category = listing.getAttribute('data-category');
        if (showList && showLocation && (selectedTag === 'all' || category === selectedTag)) {
          listing.style.display = 'flex';
        } else {
          listing.style.display = 'none';
        }
      });
    });






  <label for="filter-location"class="filter-label">Filter by location:</label>
  <select id="filter-location"class="filter-select">
    <option value="all">All</option>
    <option value="alabama">Alabama</option>
    <option value="alaska">Alaska</option>
    <option value="arizona">Arizona</option>
    <option value="arkansas">Arkansas</option>
    <option value="california">California</option>
    <option value="colorado">Colorado</option>
    <option value="connecticut">Connecticut</option>
    <option value="delaware">Delaware</option>
    <option value="florida">Florida</option>
    <option value="georgia">Georgia</option>
    <option value="hawaii">Hawaii</option>
    <option value="idaho">Idaho</option>
    <option value="illinois">Illinois</option>
    <option value="indiana">Indiana</option>
    <option value="iowa">Iowa</option>
    <option value="kansas">Kansas</option>
    <option value="kentucky">Kentucky</option>
    <option value="louisiana">Louisiana</option>
    <option value="maine">Maine</option>
    <option value="maryland">Maryland</option>
    <option value="massachusetts">Massachusetts</option>
    <option value="michigan">Michigan</option>
    <option value="minnesota">Minnesota</option>
    <option value="mississippi">Mississippi</option>
    <option value="missouri">Missouri</option>
    <option value="montana">Montana</option>
    <option value="nebraska">Nebraska</option>
    <option value="nevada">Nevada</option>
    <option value="new-hampshire">New Hampshire</option>
    <option value="new-jersey">New Jersey</option>
    <option value="new-mexico">New Mexico</option>
    <option value="new-york">New York</option>
    <option value="north-carolina">North Carolina</option>
    <option value="north-dakota">North Dakota</option>
    <option value="ohio">Ohio</option>
    <option value="oklahoma">Oklahoma</option>
    <option value="oregon">Oregon</option>
    <option value="pennsylvania">Pennsylvania</option>
    <option value="rhode-island">Rhode Island</option>
    <option value="south-carolina">South Carolina</option>
    <option value="south-dakota">South Dakota</option>
    <option value="tennessee">Tennessee</option>
    <option value="texas">Texas</option>
    <option value="utah">Utah</option>
    <option value="vermont">Vermont</option>
    <option value="virginia">Virginia</option>
    <option value="washington">Washington</option>
    <option value="west-virginia">West Virginia</option>
    <option value="wisconsin">Wisconsin</option>
    <option value="wyoming">Wyoming</option>
  </select>
