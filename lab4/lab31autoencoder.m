%lab4
 
clear
close all
clc
bindata = (csvread('bindigit_trn.csv'))';
bindata = reshape(bindata,28,28,8000);
bindata = num2cell(bindata,[1,2]);
bindatatarget = csvread('targetdigit_trn.csv');
bintestdata = csvread('bindigit_tst.csv')';
bintestdata = reshape(bintestdata,28,28,2000);
bintestdata = num2cell(bintestdata,[1,2]);
bintestdatatarget = csvread('targetdigit_tst.csv');
%imagesc(p1)
figure(1);
number_index = 0;
for i = [1,2,3,4,6,7,8,9,15]
    number_index = number_index +1
    bintestdatatarget(i)
    subplot(3,3,number_index);
    imshow(bintestdata{i});
end

autoenc = trainAutoencoder(bindata,100);
Y = predict(autoenc,bintestdata);
figure(2)
%imshow(reshape(Y(k,:),28,28));
h = plotWeights(autoenc);
figure(3)
number_index = 0;
for i = [1,2,3,4,6,7,8,9,15]
    number_index = number_index +1
    subplot(3,3,number_index);
    imshow(Y{i});
end