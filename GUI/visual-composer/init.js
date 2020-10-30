const editor = grapesjs.init({
  // Indicate where to init the editor. You can also pass an HTMLElement
  container: '#vc-editor',
  // Get the content for the canvas directly from the element
  // Size of the editor
  height: '80vh',
  width: 'auto',

  plugins:['gjs-preset-webpage'],
  // Avoid any default panel
  panels: { defaults: [] },

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
  }
});

