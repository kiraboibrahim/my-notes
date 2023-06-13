/*

    Code taken from https://w3bits.com/css-grid-masonry/
*/

function resizeMasonryItem(gridItem){
    /* Get the grid object, its row-gap, and the size of its implicit rows */
    const grid = document.getElementsByClassName("masonry")[0],
        rowGap = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-row-gap')),
        rowHeight = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-auto-rows'));
    /*
     * Spanning for any brick = S
     * Grid's row-gap = G
     * Size of grid's implicitly create row-track = R
     * Height of item content = H
     * Net height of the item = H1 = H + G
     * Net height of the implicit row-track = T = G + R
     * S = H1 / T
     */
    const rowSpan = Math.ceil((gridItem.querySelector(".masonry-content").getBoundingClientRect().height + rowGap) / (rowHeight + rowGap));

    /* Set the spanning as calculated above (S) */
    gridItem.style.gridRowEnd = 'span ' + rowSpan;
}

function resizeAllMasonryItems() {
    // Get all item class objects in one list
    const allGridItems = document.getElementsByClassName("masonry-brick");

    /*
     * Loop through the above list and execute the spanning function to
     * each list-item (i.e. each masonry item)
     */
    for (let i = 0; i < allGridItems.length; i++) {
        resizeMasonryItem(allGridItems[i]);
    }
}

function waitForImages(){
    const allItems = document.getElementsByClassName("masonry-brick");
    for(let i=0; i<allItems.length; i++){
    imagesLoaded( allItems[i], function(instance) {
        const item = instance.elements[0];
        resizeMasonryItem(item);
    } );
  }
}

const masonryEvents = ['load', 'resize'];
masonryEvents.forEach( function(event) {
  window.addEventListener(event, resizeAllMasonryItems);
});
waitForImages();