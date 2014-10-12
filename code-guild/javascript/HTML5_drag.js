//create a nodelist
var boxes = document.querySelectorAll('#drag-these .drag-and-drop');

//create an array to push the nodes into
var boxesArray = [];

//move nodes into an array
for (var i = 0; i < boxes.length; i++) {
  boxesArray.push(boxes[i]);
}

//used to store the element that drag initiates from
var dragSourceElement = null;

//event handler for the beginning of the drag
function handleDragStart (e) {
  //change opacity for feedback
  this.style.opacity = '0.75'
  
  dragSourceElement = this;
  
  //capture the inner HTML data from the element initiating the drag
  e.dataTransfer.effectAllowed = 'move';
  e.dataTransfer.setData('text/html', this.innerHTML);
}

//this handler allows us to drop an element when it is over a droppable area
function handleDragOver (e) {
  if (e.preventDefault) {
    e.preventDefault();
  }
  e.dataTransfer.dropEffect = 'move';
  return false;
}

//these handlers will toggle the over class to indicate where something can be
//dropped to
function handleDragEnter (e) {
  this.classList.add('over');
}

function handleDragLeave (e) {
  this.classList.remove('over');
}

//allow the drop and prevent bubbling
function handleDrop (e) {
  if (e.stopPropagation) {
    e.stopPropagation();
  }
  
  //check if the element being dropped onto is the source element of hte drag
  if (dragSourceElement != this) {
    //set the element being dropped to the data stored from the initiator
    dragSourceElement.innerHTML = this.innerHTML;
    this.innerHTML = e.dataTransfer.getData('text/html');
  }
  return false;
}

//remove the over class after the drop
function handleDragEnd (e) {
  boxesArray.forEach(function (node) {
    node.classList.remove('over');
  });
}

//add event listeners to each node to handle dragging events
boxesArray.forEach(function (node) {
  node.addEventListener('dragstart', handleDragStart, false);
  node.addEventListener('dragenter', handleDragEnter, false);
  node.addEventListener('dragover', handleDragOver, false);
  node.addEventListener('dragleave', handleDragLeave, false);
  node.addEventListener('drop', handleDrop, false);
  node.addEventListener('dragend', handleDragEnd, false);
});

