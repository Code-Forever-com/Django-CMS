let blockManager = editor.BlockManager;

function addBlock(id, opt) {
    blockManager.add(id, opt);
}



blockManager.add('my-first-block', {
    label: 'Simple block',
    content: {
        type:"div",
        content:"test block",
        script: function(){
            this.className = ""
    },
    },
    render: ({ model }) => `Preview
    <div style="border:1px solid gray;padding:.3rem">
        ${model.get('content')}
        </div>
    `
});

const two_col =  blockManager.add('2-col', {
    label: '2 Columns',
    category: "Basic",
    icon: `<i class="fa fa-pencil" style="font-size:2.5rem"></i>`,

    content: ` '<div class="row" data-gjs-droppable=".row-cell" data-gjs-custom-name="Row">
    <div class="row-cell" data-gjs-draggable=".row"></div> 
    <div class="row-cell" data-gjs-draggable=".row"></div> 
  </div>
    <style>.container{
        height:5rem;
        width: 50rem;
        margin: 0 auto;
    }
    .row{
        height:5rem;
        width: %100;
        margin: 0 -15px 0 -15px;
        display:flex;
        flex-wrap:wrap;
    }
    .col{
        -ms-flex-preferred-size: 0;
    flex-basis: 0;
    -ms-flex-positive: 1;
    flex-grow: 1;
    max-width: 100%;
    }
    </style>`,
    render: ({ model }) => `
    Two Column
    <div>
    ${model.get("icon")}
    </div>
    
    `

});



const styleManager = editor.StyleManager;

