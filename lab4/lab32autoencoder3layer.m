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


autoenc1 = trainAutoencoder(bindata,75,'MaxEpochs',40, ...
    'L2WeightRegularization',0.004, ...
    'SparsityRegularization',4, ...
    'SparsityProportion',0.15, ...
    'ScaleData', false);
feat1 = encode(autoenc1,bindata);
autoenc2 = trainAutoencoder(feat1,35,'MaxEpochs',20, ...
    'L2WeightRegularization',0.002, ...
    'SparsityRegularization',4, ...
    'SparsityProportion',0.1, ...
    'ScaleData', false);
feat2 = encode(autoenc2,feat1);
autoenc3 = trainAutoencoder(feat2,20,'MaxEpochs',10, ...
    'L2WeightRegularization',0.002, ...
    'SparsityRegularization',4, ...
    'SparsityProportion',0.1, ...
    'ScaleData', false);


feat3 = encode(autoenc3,feat2);
softnet = trainSoftmaxLayer(feat3,bindatatarget','MaxEpochs',40);
deepnet = stack(autoenc1,autoenc2,autoenc3,softnet);
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
plotconfusion(bintestdatatarget',y);
title("confusion plot 3 layer autoencoder")

deepnet = train(deepnet,bintrain,bindatatarget');

y = deepnet(binTest);
figure(2)
plotconfusion(bintestdatatarget',y);
title("confusion plot 3 layer autoencoder backproptuned")

%figure(3)
%h = plotWeights(autoenc2);
