%lab4
 
clear
close all
clc

% Get the number of pixels in each image
imageWidth = 28;
imageHeight = 28;
inputSize = imageWidth*imageHeight;

bindata = (csvread('bindigit_trn.csv'))';
bindata = reshape(bindata,28,28,8000);
bindata = num2cell(bindata,[1,2]);
bindatatarget = csvread('targetdigit_trn.csv');
bintestdata = csvread('bindigit_tst.csv')';
bintestdata = reshape(bintestdata,28,28,2000);
bintestdata = num2cell(bintestdata,[1,2]);
bintestdatatarget = csvread('targetdigit_tst.csv');
%imagesc(p1)
number_index = 0;
target = zeros(8000,10);
targettest = zeros(2000,10);

for i = 1:8000
    j = bindatatarget(i)+1;
    target(i,j) = 1;
end
for i = 1:2000
    j = bintestdatatarget(i)+1;
    targettest(i,j) = 1;
end

autoenc1 = trainAutoencoder(bindata,75,'MaxEpochs',40, ...
    'L2WeightRegularization',0.004, ...
    'SparsityRegularization',4, ...
    'SparsityProportion',0.15, ...
    'ScaleData', false);
feat1 = encode(autoenc1,bindata);



softnet = trainSoftmaxLayer(feat1,target','MaxEpochs',40);
deepnet = stack(autoenc1,softnet);
view(deepnet)



% Turn the test images into vectors and put them in a matrix
binTest = zeros(inputSize,numel(bintestdata));
for i = 1:numel(bintestdata)
    binTest(:,i) = bintestdata{i}(:);
end

% Turn the training images into vectors and put them in a matrix
bintrain = zeros(inputSize,numel(bindata));
for i = 1:numel(bindata)
    bintrain(:,i) = bindata{i}(:);
end
% Perform fine tuning

figure(1)
y = deepnet(binTest);
plotconfusion(targettest',y);
title("confusion plot 1 layer autoencoder")

deepnet = train(deepnet,bintrain,target');

y = deepnet(binTest);
figure(2)
plotconfusion(targettest',y);
title("confusion plot 1 layer autoencoder backproptuned")

%figure(3)
%h = plotWeights(autoenc2);