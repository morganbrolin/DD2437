function [ E ] = energy( W, X )
    E = -X * W * X';
end

