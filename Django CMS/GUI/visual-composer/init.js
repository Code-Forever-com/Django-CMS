const editor = grapesjs.init({
  // Indicate where to init the editor. You can also pass an HTMLElement
  container: '#vc-editor',
  // Get the content for the canvas directly from the element
  // Size of the editor
  height: '80vh',
  width: 'auto',
  // Disable the storage manager for the moment
  storageManager: {
    id: 'gjs-',             // Prefix identifier that will be used on parameters
    type: 'session',          // Type of the storage
    autosave: true,         // Store data automatically
    autoload: true,         // Autoload stored data on init
    stepsBeforeSave: 5,     // If autosave enabled, indicates how many changes are necessary before store method is triggered
  },
  // Avoid any default panel
  panels: { defaults: [] },
  blockManager: {
    appendTo: '#blocks',
  },
  styleManager: {
    appendTo: '#styles',
    sectors: [{
      name: "Dimension",
      open: false,
      buildProps: ["width", "min-height", "padding"],
      properties: [{
        type: 'integer',
        name: 'The width',
        property: "width",
        units: ["px", "%", "vw","rem"],
        defaults: "auto",
        min: 0
      }]
    },
    {
      name: "Color",
      open: false,
      buildProps: ["color", "background-color"],
      properties: [{
        type: 'color',
        name: 'Text Color',
        property: "color",
        units: [],
        defaults: "black"
      },
      {
        type: 'color',
        name: 'Background Color',
        property: "background-color",
        units: [],
        defaults: "white"
      },
      ]
    },
    {
      name: "Font",
      open: false,
      buildProps: ["font-family", "font-size","font-weight"],
      properties: [{
        type: 'select',
        name: 'Font Size',
        property: "font-size",
        list:[
          {value:"xx-small"},
          {value:"x-small"},
          {value:"smaller"},
          {value:"small"},
          {value:"medium"},
          {value:"large"},
          {value:"larger"},
          {value:"x-large"},
          {value:"xx-large"},
        ]
      },
      ]
    },
    {
      name: "Background",
      open: false,
      buildProps: ["background-image","background-position","background-attachment","background-repeat","background-size"],
      properties: [{
        type: 'file',
        name: 'Background Image',
        property: "background-image",
        units: [],
        defaults: ""
      }
      ]
    },
  ]
  },
  traitManager:{
    appendTo:"#traits"
  },
  layerManager:{
    appendTo:"#layers"
  }
});

