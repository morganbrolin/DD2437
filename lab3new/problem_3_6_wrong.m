
clear
close all
clc

%% Load pict.dat

A = importdata('pict.dat');
P = zeros(11,1024);

for i = 1: 1: length(A)
    if (i/1024) - floor(i/1024) == 0
        k = floor(i/1024);
    else 
        k = floor(i/1024)+1;
    end
    P(k,(i-(k-1)*1024)) = A(i);
end
biasoffset = 0.5;
%bias can only have values -0.49999 to + 0.49999 and then plus 0.5(offset)
%    0.4 gives 10%  0.45 gives p = 5%   0.49 gives 1%
fig_num = 0
for i = 1:199
    bias_pattern = i*0.005-0.5 + biasoffset;
    X_train = sign(sign(rand(300,100)-bias_pattern)+1);
    ite_max = 10;
    az = size(X_train);
    Pz = az(1);
    Nz = az(2);
    activity = (1/(Nz*Pz))*sum(sum(X_train))
    if or(and((activity < 0.11),( activity > 0.09)),and((activity < 0.91),( activity > 0.89)))
        ratioArray = [];
        Iarray_bias = [];
        for ii = 1:199
            bias = ii*0.005-0.5 + biasoffset;
            stabel_patterns = weight_update_seqdata_batch_sparse_p_plot_wrong(X_train, ite_max,bias,activity);
            ratioArray = [ratioArray stabel_patterns];
            Iarray_bias = [Iarray_bias bias];
            
            

        end
            fig_num = fig_num +1;
            figure(fig_num)
            plot(Iarray_bias,ratioArray)
            title("Bias: "+bias_pattern+"activity: "+activity)
            xlabel('Bias') % x-axis label
            ylabel('Capacity') % y-axis label
    end
        if or(and((activity < 0.06),( activity > 0.04)),and((activity < 0.96),( activity > 0.94)))
        ratioArray = [];
        Iarray_bias = [];
        for ii = 1:199
            bias = ii*0.005-0.5 + biasoffset;
            stabel_patterns = weight_update_seqdata_batch_sparse_p_plot_wrong(X_train, ite_max,bias,activity);
            ratioArray = [ratioArray stabel_patterns];
            Iarray_bias = [Iarray_bias bias];
            
            

        end
            fig_num = fig_num +1;

            figure(fig_num)
            plot(Iarray_bias,ratioArray)
            title("Bias: "+bias_pattern+"activity: "+activity)
            xlabel('Bias') % x-axis label
            ylabel('Capacity') % y-axis label
        end
    if or(and((activity < 0.011),( activity > 0.009)),and((activity < 0.991),( activity > 0.989)))
        ratioArray = [];
        Iarray_bias = [];
        for ii = 1:199
            bias = ii*0.005-0.5 + biasoffset;
            stabel_patterns = weight_update_seqdata_batch_sparse_p_plot_wrong(X_train, ite_max,bias,activity);
            ratioArray = [ratioArray stabel_patterns];
            Iarray_bias = [Iarray_bias bias];
            
            

        end
            fig_num = fig_num +1;
            figure(fig_num)
            plot(Iarray_bias,ratioArray)
            title("Bias: "+bias_pattern+"activity: "+activity)
            xlabel('Bias') % x-axis label
            ylabel('Capacity') % y-axis label
       
    end
end


%X_test = [reshape(P10,[1, 1024])];



    
