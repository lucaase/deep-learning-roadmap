clear all

dt = 1/32552;
aux = dir;

spk_wvf = [];
for i = 3:size(aux,1)
    FileBase = aux(i).name;
    [~,G] = LoadCluRes(FileBase,1:8,[]);
    
    for shank = 1:8
        % Load spike waveforms and clusters from current shank
        spk = LoadSpk([FileBase '.spk.' num2str(shank)],8,54);
        clu = LoadClu([FileBase '.clu.' num2str(shank)]);
        spk2 = squeeze(spk(:,:,clu>1));
        
        % Get waveforms from the channels with their maximal amplitude
        for wvf = 1:size(spk2,3)
            [~, ch] = max(abs(spk2(:,27,wvf)));
            spk_wvf(:,end+1) = [spk2(ch,:,wvf),G(wvf)];
        end
    end
end

spk_wvf = spk_wvf';