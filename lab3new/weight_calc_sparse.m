function [ W,activity ] = weight_calc_sparse( patterns, normalize, correct_diag)

[P,N] = size(patterns);

if nargin < 3
    correct_diag = true;
end

if nargin <2
    normalize = false;
end


activity = (1/(N*P))*sum(sum(patterns));
patterns = patterns - activity;
W = patterns'*patterns;
Wsum =sum(sum(W));

if normalize
    W = W./N;
end

if correct_diag
        N = size(W,1);
    W(1:N+1:end)=0
end

end