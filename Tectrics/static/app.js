//import * as THREE from '../three.js-master/build/three.module.js';
import * as THREE from './three.module.js';
//import { OrbitControls } from "../three.js-master/examples/jsm/controls/OrbitControls.js";
import {OrbitControls} from './OrbitControls.js';
// import {TrackballControls} from './TrackballControls.js';

// 카메라를 Z축 주위로 회전시키는 함수

function createContainer(width, height, depth, color) {
    const geometry = new THREE.BoxGeometry(width, height, depth);
    const material = new THREE.MeshBasicMaterial({
        color: color,
        wireframe: true,
        transparent: true,
        opacity: 0.5
    });
    const container = new THREE.Mesh(geometry, material);

    // 컨테이너의 중심이 원점에 위치하도록 설정
    container.position.set(width / 2, height / 2, depth / 2);
    return container;
}

// 상자와 외곽선을 만드는 함수
function createBoxWithEdges(width, height, depth, color) {
    // 상자 생성
    const geometry = new THREE.BoxGeometry(width, height, depth);
    const material = new THREE.MeshBasicMaterial({ color:color, transparent : true, opacity: 0.7});
    const box = new THREE.Mesh(geometry, material);

    // 상자 외곽선 생성
    const edges = new THREE.EdgesGeometry(geometry);
    const edgesMaterial = new THREE.LineBasicMaterial({ color: 0x000000 });
    const edgesMesh = new THREE.LineSegments(edges, edgesMaterial);

    // 상자와 외곽선을 하나의 그룹으로 묶음
    const group = new THREE.Group();
    group.add(box);
    group.add(edgesMesh);

    return group;
}

function createCustomGrid(width, height, divisionsWidth, divisionsHeight, color) {
    const gridHelper = new THREE.Group();
    const stepWidth = width / divisionsWidth;
    const stepHeight = height / divisionsHeight;

    const material = new THREE.LineBasicMaterial({ color: color });

    // 수평선 생성
    for (let i = 0; i <= divisionsHeight; i++) {
        const horizontalPoints = [
            new THREE.Vector3(0, i * stepHeight, 0),
            new THREE.Vector3(width, i * stepHeight, 0)
        ];
        const geometryH = new THREE.BufferGeometry().setFromPoints(horizontalPoints);
        const horizontalLine = new THREE.Line(geometryH, material);
        gridHelper.add(horizontalLine);
    }

    // 수직선 생성
    for (let j = 0; j <= divisionsWidth; j++) {
        const verticalPoints = [
            new THREE.Vector3(j * stepWidth, 0, 0),
            new THREE.Vector3(j * stepWidth, height, 0)
        ];
        const geometryV = new THREE.BufferGeometry().setFromPoints(verticalPoints);
        const verticalLine = new THREE.Line(geometryV, material);
        gridHelper.add(verticalLine);
    }

    return gridHelper;
}


class App {
    

    constructor () {
        const divContainer = document.querySelector("#webgl-container");
        this._divContainer = divContainer; /*밑줄로 시작하는 필드와 매서드는 private으로 클래스 외부에서 호출 불가 */

        const renderer = new THREE.WebGLRenderer({antialias: true});
        renderer.setPixelRatio(window.devicePixelRatio);
        divContainer.appendChild(renderer.domElement);
        this._renderer = renderer;

        const scene = new THREE.Scene();
        this._scene = scene;

        this._setupCamera(); /*카메라 매서드 호출, 밑줄로 시작하는 */
        this._setupLight();
        this._setupModel();
        this._setupControls();

        window.onresize = this.resize.bind(this);
        this.resize();

        requestAnimationFrame(this.render.bind(this));
        
        this.rotateCameraOnZAxis(Math.PI / 4);

}
rotateCameraOnZAxis(angle) {
    const quaternion = new THREE.Quaternion();
    quaternion.setFromAxisAngle(new THREE.Vector3(0, 0, 1), angle);
    this._camera.quaternion.multiplyQuaternions(quaternion, this._camera.quaternion);
    this._camera.quaternion.normalize();
    this._controls.update();
}


// JSON 파일에서 로드하는 직육면체를 생성하는 함수
_loadCubesFromJson() {
    // fetch('../static/packed_items.json')
    fetch('../static/packed_items.json')
      .then(response => response.json())
      .then(data => {
        data.forEach(item => {
          // 직육면체의 중심 좌표를 계산합니다.
          const centerX = item.positionX + item.width / 2;
          const centerY = item.positionY + item.height / 2;
          const centerZ = item.positionZ + item.depth / 2;
        
        const boxWithEdges = createBoxWithEdges(item.width, item.height, item.depth, item.color, 0.5);
        boxWithEdges.position.set(centerX, centerY, centerZ);

        this._scene.add(boxWithEdges);
    });

      })
      .catch(error => {
        console.error('Error loading JSON:', error);
      });
}

_setupCamera() {
    const width = this._divContainer.clientWidth;
    const height = this._divContainer.clientHeight;
    const depth = this._divContainer.clientDepth;
    const camera = new THREE.PerspectiveCamera(
        60,
        width / height,
        1,
        100000
    );
    camera.position.set(2000, 4000, 5000); // x = 0, y = 20, z = 0 위치로 설정
    camera.lookAt(new THREE.Vector3(2500, 2500,0)); // 카메라가 원점을 바라보도록 설정
    
    this._camera = camera;
}

_setupLight() {

    this._scene.background = new THREE.Color(0xffffff);
    //주변 조명 
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    this._scene.add(ambientLight);

    
    const directionLight = new THREE.DirectionalLight(0xffffff, 0.5);
    directionLight.position.set(-1,2,4);
    this._scene.add(directionLight);
}

_createLabel(text, position = new THREE.Vector3(0,0,0)) {
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    const canvasSize = 128;

    context.font = '20px Arial';
    context.textAlign = 'center';
    context.textBaseline = 'middle';
    context.fillStyle = 'black';
    context.fillText(text, canvasSize / 2, canvasSize / 2);

    const texture = new THREE.CanvasTexture(canvas);
    const material = new THREE.SpriteMaterial({ map: texture });
    const sprite = new THREE.Sprite(material);

    // 원점에 라벨 위치 설정
    sprite.position.copy(position);
    sprite.scale.set(3, 3, 3);  // 크기 조절

    return sprite;
}


_setupModel() {

    const customGrid = createCustomGrid(2700, 1600, 16, 27, 0x888888); // 어두운 회색으로 그리드 생성
customGrid.position.set(0, 0, 0); // 그리드 위치 설정 (원점)
this._scene.add(customGrid);

    const containerWidth = 2700;
    const containerHeight = 1600;
    const containerDepth = 1600;
    const containerColor = 0xaaaaaa;  // 회색

    // 컨테이너 생성 및 추가
    const container = createContainer(containerWidth, containerHeight, containerDepth, containerColor);
    this._scene.add(container);


    const axesHelper = new THREE.AxesHelper(15);
this._scene.add(axesHelper);



    // 기존 모델 설정 코드
    // ...

    //축을 직접 생성
    const axes = new THREE.Group();
    const xAxisMaterial = new THREE.LineBasicMaterial({ color: 0xff0000, linewidth: 10 }); // 빨간색 X축
    const yAxisMaterial = new THREE.LineBasicMaterial({ color: 0x00ff00, linewidth: 10}); // 초록색 Y축
    const zAxisMaterial = new THREE.LineBasicMaterial({ color: 0x0000ff, linewidth: 5 }); // 파란색 Z축

    const axisLength = 1000;
    const xAxisGeometry = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0, 0, 0), new THREE.Vector3(axisLength, 0, 0)]);
    const yAxisGeometry = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0, 0, 0), new THREE.Vector3(0, axisLength, 0)]);
    const zAxisGeometry = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0, 0, 0), new THREE.Vector3(0, 0, axisLength)]);

    const xAxis = new THREE.Line(xAxisGeometry, xAxisMaterial);
    const yAxis = new THREE.Line(yAxisGeometry, yAxisMaterial);
    const zAxis = new THREE.Line(zAxisGeometry, zAxisMaterial);

    axes.add(xAxis);
    axes.add(yAxis);
    axes.add(zAxis);

    this._scene.add(axes);

    // 나머지 모델 추가 코드
    // ...


    
        // 기존 모델 설정 코드
        // ...
    
        this._loadCubesFromJson(); // JSON 파일에서 직육면체 로드 및 생성
    

}

_setupCamera() {
    const width = this._divContainer.clientWidth;
    const height = this._divContainer.clientHeight;
    const depth = this._divContainer.clientDepth;
    const camera = new THREE.PerspectiveCamera(
        60,
        width / height,
        1,
        100000
    );
    camera.position.set(2000, 4000, 5000); // x = 0, y = 20, z = 0 위치로 설정
    camera.lookAt(new THREE.Vector3(2500, 2500,0)); // 카메라가 원점을 바라보도록 설정
    
    this._camera = camera;
}

_setupControls() {
        // OrbitControls 설정
// this._controls = new TrackballControls(this._camera, this._divContainer);

//     // 수직축(Y축) 회전 제한 해제
//     this._controls.minPolarAngle = 0;  // 하단 제한 없음
//     this._controls.maxPolarAngle = Math.PI;  // 상단 제한 없음

//     // 수평축(X축) 회전 제한 해제
//     this._controls.minAzimuthAngle = -Infinity;  // 왼쪽 회전 제한 없음
//     this._controls.maxAzimuthAngle = Infinity;  // 오른쪽 회전 제한 없음
// // X축을 중심으로 회전 제한
// //this._controls.minPolarAngle = -Math.PI/2; // 하단 제한
// //this._controls.maxPolarAngle = Math.PI / 2; // 상단 제한
// this._controls.target.set(5,5,5);
// // 초기화
// this._controls.update();
    // // OrbitControls 객체를 생성하고 this._controls로 할당
    this._controls = new OrbitControls(this._camera, this._divContainer);

    // // 관성 효과를 사용하여 더 부드러운 컨트롤 제공
    this._controls.enableDamping = true;
    this._controls.dampingFactor = 0.05;

    // // 화면 공간 패닝 비활성화
    this._controls.screenSpacePanning = false;

    // 줌 인/아웃 가능 거리 설정
    // this._controls.minDistance = 5;
    // this._controls.maxDistance = 50;

    // 카메라가 올라갈 수 있는 최대 각도
    //this._controls.maxPolarAngle = Math.PI / 2;

    // 회전, 줌, 패닝 속도 설정
    // this._controls.rotateSpeed = 1.0;
    // this._controls.zoomSpeed = 1.2;
    // this._controls.panSpeed = 0.8;

    this._controls.update();

    // 패닝 키 설정
    // this._controls.keys = {
    //     LEFT: 'ArrowLeft',
    //     RIGHT: 'ArrowRight',
    //     UP: 'ArrowUp',
    //     DOWN: 'ArrowDown'
    // };
}
rotateCameraOnZAxis(angle) {
    // 카메라의 현재 쿼터니언에 Z축 회전 추가
    const quaternion = new THREE.Quaternion();
    quaternion.setFromAxisAngle(new THREE.Vector3(0, 0, 1), angle);
    this._camera.quaternion.multiplyQuaternions(quaternion, this._camera.quaternion);
    this._camera.quaternion.normalize();

    // 컨트롤 업데이트
    this._controls.update();
}
resize() {
    const width = this._divContainer.clientWidth;
    const height = this._divContainer.clientHeight;

    this._camera.aspect = width / height;
    this._camera.updateProjectionMatrix();

    this._renderer.setSize(width, height);
}

render(time) {
    this._renderer.render(this._scene, this._camera);
    this.update(time);
    requestAnimationFrame(this.render.bind(this));
}

update(time) {
    time *=0.001;
    // this._cube.rotation.x = time;
    // this._cube.rotation.y = time;
}
}

window.onload = function() {
new App();
}