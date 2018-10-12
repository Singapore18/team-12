import React, { Component } from 'react';
import './index.css';
import Stepper from 'react-stepper-horizontal';
import { ButtonToolbar, DropdownButton, MenuItem, Button } from 'react-bootstrap';
import './bootstrap.css';
import emoji1 from './pic/emoji1.png';
import emoji2 from './pic/emoji2.png';
import emoji3 from './pic/emoji3.png';
import emoji4 from './pic/emoji4.png';
import emoji5 from './pic/emoji5.png';
import emoji6 from './pic/emoji6.png';
import emoji7 from './pic/emoji7.png';
import C1_Score from './pic/C1_Score.png';
import C2 from './pic/C2.png';
import G1_Score from './pic/G1_Score.png';
import G2_Score from './pic/G2_Score.png';
import P2 from './pic/P2.png';
import S1 from './pic/S1.png';
import S2 from './pic/S2.png';
import S3_Score from './pic/S3_Score.png';
import T1 from './pic/T1.png';
import T2_Score from './pic/T2_Score.png';


class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      op1: 1,
      op2: 0.5,
      op3: 0.5,
      op4: 0.5,
      op5: 0.5,
      // text: '{' +
      //   '"data": ' +
      //   '[' +
      //   '{"surveyid": 1,"questionid": 1,"questiontext": "I have a certain amount of intelligence, and I cannot really do much to change it.","category": 1,"isScale": 1,"scale": 7,"reversed": 0,"options": ["string", "string", "string", "string"]},' +
      //   '{"surveyid": 1,"questionid": 2,"questiontext": "My intelligence is something that I cannot change very much.","category": 1,"isScale": 1,"scale": 7,"reversed": 0,"options": ["string", "string", "string", "string"]},' +
      //   '{"surveyid": 1,"questionid": 1,"questiontext": "1: have a certain amount of intelligence, and I cannot really do much to change it.","category": 1,"isScale": 1,"scale": 7,"reversed": 0,"options": ["string", "string", "string", "string"]},' +
      //   '{"surveyid": 1,"questionid": 2,"questiontext": "2:  intelligence is something that I cannot change very much.","category": 1,"isScale": 1,"scale": 7,"reversed": 0,"options": ["string", "string", "string", "string"]},' +
      //   '{"surveyid": 1,"questionid": 2,"questiontext": "My intelligence is something that I cannot change very much.","category": 1,"isScale": 1,"scale": 7,"reversed": 0,"options": ["string", "string", "string", "string"]}' +
      //   ']' +
      //   '}',

      init: 0,
      obj: '',
      black: true,
      steps: [{
        title: 'Level 1',
        href: 'http://example1.com',
        onClick: (e) => {
          e.preventDefault()
          console.log('onClick', 1)
        }
      }, {
        title: 'Level 2',
        href: 'http://example2.com',
        onClick: (e) => {
          e.preventDefault()
          console.log('onClick', 2)
        }
      }, {
        title: 'Level 3',
        href: 'http://example3.com',
        onClick: (e) => {
          e.preventDefault()
          console.log('onClick', 3)
        }
      }, {
        title: 'Level 4',
        href: 'http://example4.com',
        onClick: (e) => {
          e.preventDefault()
          console.log('onClick', 4)
        }
      }],
      currentStep: 0,
      dashboard:true,
    }
    this.onClickNext = this.onClickNext.bind(this);
    this.dashboard = this.dashboard.bind(this);
    this.question = this.question.bind(this);
  }

  changeOpacity = (e) => {

    var st = e;
    if (st === "op1") {
      this.setState({ op1: 1, op2: 0.5, op3: 0.5, op4: 0.5, op5: 0.5, init:0 });
    } else if (st === "op2") {
      this.setState({ op1: 0.5, op2: 1, op3: 0.5, op4: 0.5, op5: 0.5, init:5  });
    } else if (st === "op3") {
      this.setState({ op1: 0.5, op2: 0.5, op3: 1, op4: 0.5, op5: 0.5, init:10 });
    } else if (st === "op4") {
      this.setState({ op1: 0.5, op2: 0.5, op3: 0.5, op4: 1, op5: 0.5, init:15 });
    } else if (st === "op5") {
      this.setState({ op1: 0.5, op2: 0.5, op3: 0.5, op4: 0.5, op5: 1, init:20 });
    }

  }

  changeSection = (e) => {
    var st = e;
    if (st === "level1") {

    }
  }

  onClickNext() {
    const { steps, currentStep } = this.state;
    this.setState({
      currentStep: currentStep + 1,
    });
  }

  start() {
    var self = this;
    fetch('http://54.169.81.203/questions/1')
      .then(results => {
        return results.json();
      })
      .then(data => {
        //console.log(results.json());
        self.setState({ obj: data });
        console.log(self.state.obj);
      });
  }

  changeColor() {
    this.setState({ black: !this.state.black })
  }

  question(){
    this.setState({dashboard:true});
  }


  
  dashboard(){
    this.setState({dashboard:false});
    console.log(this.state.dashboard)
  }


  render() {

    let top = this.state.black ? "blackButton" : "whiteButton";

    // var obj = JSON.parse(this.state.text);

    var obj = this.state.obj;
    var qnArr = [];
    var isScale = [];

    for (var i = this.state.init; i < obj.length && i <= this.state.init + 4; i++) {
      console.log(obj[i]["questiontext"]);
      qnArr.push(obj[i]["questiontext"]);
      isScale.push(obj[i]["isScale"]);

      // you need to write each key name here
    } // onclick the level change the init

    const { steps, currentStep } = this.state;


    return (
      <div className="App">
      {this.state.dashboard?
      <div><Button bsStyle = "danger"  onClick={() => this.start()}> Start Challenge </Button>
      <Button bsStyle="success" style={{float:"right"}}onClick={this.dashboard }>Go to Dashboard (Admin) </Button>
        {/* <div class="topnav">
          <a className = {top} style={{borderRadius: "50%"}} href="#home" onClick={this.changeColor.bind(this)}>Level 1</a>
          <a href="#news" onClick={() => this.changeSection("level2")}>Level 2</a>
          <a href="#contact" onClick={() => this.changeSection("level3")}>Level 3</a>
          <a href="#about" onClick={() => this.changeSection("level4")}>Level 4</a>
        </div> */}

        <div style={{backgroundColor:"orange", marginRight:"200px",marginLeft:"200px"}}>
          <Stepper steps={steps} activeStep={currentStep} />
          
        </div>
        <div style={{textAlign:"center"}}>
        <Button bsStyle="success" style={{float:"right"}}onClick={this.onClickNext }>Next</Button>
        </div>
        <div class="sidenav">
          <div class="pic" style={{ opacity: this.state.op1, backgroundColor: "white", marginBottom: "20px" }}><input type="image" style={{ width: "90px", height: "90px", margin: "auto" }} onClick={() => this.changeOpacity("op1")} src="https://www.shareicon.net/data/512x512/2015/05/27/44710_twitter_512x512.png" /></div>
          <div class="pic" style={{ opacity: this.state.op2, backgroundColor: "white", marginBottom: "20px" }}><input type="image" style={{ width: "90px", height: "90px", margin: "auto" }} onClick={() => this.changeOpacity("op2")} src="https://orig00.deviantart.net/a7f4/f/2017/330/c/0/monster_hunter_world_icon__10__by_malfacio-dbuwzv6.png" /></div>

          <div class="pic" style={{ opacity: this.state.op4, backgroundColor: "white", marginBottom: "20px" }}><input type="image" style={{ width: "90px", height: "90px", margin: "auto" }} onClick={() => this.changeOpacity("op4")} src="https://mbtskoudsalg.com/images/vector-monster-creature-3.png" /></div>
          <div class="pic" style={{ opacity: this.state.op5, backgroundColor: "white", marginBottom: "20px" }}><input type="image" style={{ width: "90px", height: "90px", margin: "auto" }} onClick={() => this.changeOpacity("op5")} src="http://inkwellideas.com/wp-content/uploads/2010/06/monsterlair.png" /></div>
        </div>
        <div class="main" style={{marginTop:"100px", marginRight:"100px"}}>


          {
            qnArr.map((number) =>
              <div style={{ fontFamily: "Oswald", fontSize: 30 }}><p>{number}</p>
              <span>
                <img src={emoji1} style={{height:35, marginRight:20}}/>
                <img src={emoji2} style={{height:35,marginRight:20}}/>
                <img src={emoji3} style={{height:35,marginRight:20}}/>
                <img src={emoji4} style={{height:35,marginRight:20}}/>
                <img src={emoji5} style={{height:35,marginRight:20}}/>
                <img src={emoji6} style={{height:35,marginRight:20}}/>
                <img src={emoji7} style={{height:35,marginRight:20}}/>
              </span>
              </div>

            )
          }


        </div>
</div> :<div>
<Button bsStyle="success" style={{float:"right"}}onClick={this.question }>Go back to question</Button>
                <img src={C1_Score} />
                <img src={C2}/>
                <img src={G1_Score}/>
                <img src={G2_Score} />
                <img src={P2} />
                <img src={S1} />
                <img src={S2} />
                <img src={S3_Score} />
                <img src={T1} />
                <img src={T2_Score} />

</div> }
        
        

</div>

      

     
    );
  }
}

export default App;
