import FWCore.ParameterSet.Config as cms
import os

from Configuration.StandardSequences.Eras import eras
process = cms.Process("PatMuonAnalyser",eras.Phase2C2)
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D13Reco_cff')

# Beware, in this area the wild character is not working!
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:FCFE6AA2-665C-E711-BDB5-5065F38172A1.root'
        #'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/FEC1FBCC-74B5-E611-A30C-0025904B793A.root'
    ),
)

process.load('RecoMuon.MuonIsolation.muonIsolationPUPPI_cff')

process.puppiNewIso = process.muonIsolationMiniAODPUPPINoLeptons.clone()
process.trkNewIso = process.puppiNewIso.clone(usePUPPI = cms.bool(False), useOnlyTrack = cms.bool(True))
process.pfNewIso = process.puppiNewIso.clone(usePUPPI = cms.bool(False))

process.minipuppiNewIso = process.puppiNewIso.clone(usePUPPI = cms.bool(True), useMiniIso = cms.bool(True))
process.minitrkNewIso = process.puppiNewIso.clone(usePUPPI = cms.bool(False), useOnlyTrack = cms.bool(True), useMiniIso = cms.bool(True))
process.minipfNewIso = process.puppiNewIso.clone(usePUPPI = cms.bool(False), useMiniIso = cms.bool(True))

"""
process.puppiNewIsoPt05 = process.puppiNewIso.clone(pfminPt = cms.double(0.5))
process.pfNewIsoPt05 = process.puppiNewIsoPt05.clone(usePUPPI = cms.bool(False))

process.puppiNewIsoPt10 = process.puppiNewIso.clone(pfminPt = cms.double(1.0))
process.pfNewIsoPt10 = process.puppiNewIsoPt10.clone(usePUPPI = cms.bool(False))

process.puppiNewIsoPt15 = process.puppiNewIso.clone(pfminPt = cms.double(1.5))
process.pfNewIsoPt15 = process.puppiNewIsoPt15.clone(usePUPPI = cms.bool(False))

process.puppiNewIsoPt20 = process.puppiNewIso.clone(pfminPt = cms.double(2.0))
process.pfNewIsoPt20 = process.puppiNewIsoPt20.clone(usePUPPI = cms.bool(False))
"""

"""
process.puppiNewIsoPt02 = process.puppiNewIso.clone(pfminPt = cms.double(0.2))
process.pfNewIsoPt02 = process.puppiNewIsoPt02.clone(usePUPPI = cms.bool(False))

process.puppiNewIsoPt04 = process.puppiNewIso.clone(pfminPt = cms.double(0.4))
process.pfNewIsoPt04 = process.puppiNewIsoPt04.clone(usePUPPI = cms.bool(False))

process.puppiNewIsoPt05 = process.puppiNewIso.clone(pfminPt = cms.double(0.5))
process.pfNewIsoPt05 = process.puppiNewIsoPt05.clone(usePUPPI = cms.bool(False))

process.puppiNewIsoPt06 = process.puppiNewIso.clone(pfminPt = cms.double(0.6))
process.pfNewIsoPt06 = process.puppiNewIsoPt06.clone(usePUPPI = cms.bool(False))

process.puppiNewIsoPt08 = process.puppiNewIso.clone(pfminPt = cms.double(0.8))
process.pfNewIsoPt08 = process.puppiNewIsoPt08.clone(usePUPPI = cms.bool(False))

process.puppiNewIsoPt10 = process.puppiNewIso.clone(pfminPt = cms.double(1.0))
process.pfNewIsoPt10 = process.puppiNewIsoPt10.clone(usePUPPI = cms.bool(False))

process.puppiNewIsoPt15 = process.puppiNewIso.clone(pfminPt = cms.double(1.5))
process.pfNewIsoPt15 = process.puppiNewIsoPt15.clone(usePUPPI = cms.bool(False))

process.puppiNewIsoPt20 = process.puppiNewIso.clone(pfminPt = cms.double(2.0))
process.pfNewIsoPt20 = process.puppiNewIsoPt20.clone(usePUPPI = cms.bool(False))
"""
process.puppiNewIsoPt02 = process.puppiNewIso.clone(pfminPt = cms.double(0.2))
process.pfNewIsoPt02 = process.puppiNewIsoPt02.clone(usePUPPI = cms.bool(False))

process.puppiNewIsoPt04 = process.puppiNewIso.clone(pfminPt = cms.double(0.4))
process.pfNewIsoPt04 = process.puppiNewIsoPt04.clone(usePUPPI = cms.bool(False))

process.puppiNewIsoPt05 = process.puppiNewIso.clone(pfminPt = cms.double(0.5))
process.pfNewIsoPt05 = process.puppiNewIsoPt05.clone(usePUPPI = cms.bool(False))

process.TFileService = cms.Service("TFileService",fileName = cms.string("out.root"))
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(200))

"""
puppiNewIsoPt05_ch = cms.InputTag("puppiNewIsoPt05","h+-DR030-ThresholdVeto000-ConeVeto000"),
puppiNewIsoPt05_nh = cms.InputTag("puppiNewIsoPt05","h0-DR030-ThresholdVeto000-ConeVeto001"),
puppiNewIsoPt05_ph = cms.InputTag("puppiNewIsoPt05","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
pfNewIsoPt05_ch = cms.InputTag("pfNewIsoPt05","h+-DR030-ThresholdVeto000-ConeVeto000"),
pfNewIsoPt05_nh = cms.InputTag("pfNewIsoPt05","h0-DR030-ThresholdVeto000-ConeVeto001"),
pfNewIsoPt05_ph = cms.InputTag("pfNewIsoPt05","gamma-DR030-ThresholdVeto000-ConeVeto001"),

puppiNewIsoPt10_ch = cms.InputTag("puppiNewIsoPt10","h+-DR030-ThresholdVeto000-ConeVeto000"),
puppiNewIsoPt10_nh = cms.InputTag("puppiNewIsoPt10","h0-DR030-ThresholdVeto000-ConeVeto001"),
puppiNewIsoPt10_ph = cms.InputTag("puppiNewIsoPt10","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
pfNewIsoPt10_ch = cms.InputTag("pfNewIsoPt10","h+-DR030-ThresholdVeto000-ConeVeto000"),
pfNewIsoPt10_nh = cms.InputTag("pfNewIsoPt10","h0-DR030-ThresholdVeto000-ConeVeto001"),
pfNewIsoPt10_ph = cms.InputTag("pfNewIsoPt10","gamma-DR030-ThresholdVeto000-ConeVeto001"),

puppiNewIsoPt15_ch = cms.InputTag("puppiNewIsoPt15","h+-DR030-ThresholdVeto000-ConeVeto000"),
puppiNewIsoPt15_nh = cms.InputTag("puppiNewIsoPt15","h0-DR030-ThresholdVeto000-ConeVeto001"),
puppiNewIsoPt15_ph = cms.InputTag("puppiNewIsoPt15","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
pfNewIsoPt15_ch = cms.InputTag("pfNewIsoPt15","h+-DR030-ThresholdVeto000-ConeVeto000"),
pfNewIsoPt15_nh = cms.InputTag("pfNewIsoPt15","h0-DR030-ThresholdVeto000-ConeVeto001"),
pfNewIsoPt15_ph = cms.InputTag("pfNewIsoPt15","gamma-DR030-ThresholdVeto000-ConeVeto001"),

puppiNewIsoPt20_ch = cms.InputTag("puppiNewIsoPt20","h+-DR030-ThresholdVeto000-ConeVeto000"),
puppiNewIsoPt20_nh = cms.InputTag("puppiNewIsoPt20","h0-DR030-ThresholdVeto000-ConeVeto001"),
puppiNewIsoPt20_ph = cms.InputTag("puppiNewIsoPt20","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
pfNewIsoPt20_ch = cms.InputTag("pfNewIsoPt20","h+-DR030-ThresholdVeto000-ConeVeto000"),
pfNewIsoPt20_nh = cms.InputTag("pfNewIsoPt20","h0-DR030-ThresholdVeto000-ConeVeto001"),
pfNewIsoPt20_ph = cms.InputTag("pfNewIsoPt20","gamma-DR030-ThresholdVeto000-ConeVeto001"),
"""
"""
    puppiNewIsoPt02_ch = cms.InputTag("puppiNewIsoPt02","h+-DR030-ThresholdVeto000-ConeVeto000"),
    puppiNewIsoPt02_nh = cms.InputTag("puppiNewIsoPt02","h0-DR030-ThresholdVeto000-ConeVeto001"),
    puppiNewIsoPt02_ph = cms.InputTag("puppiNewIsoPt02","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
    pfNewIsoPt02_ch = cms.InputTag("pfNewIsoPt02","h+-DR030-ThresholdVeto000-ConeVeto000"),
    pfNewIsoPt02_nh = cms.InputTag("pfNewIsoPt02","h0-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt02_ph = cms.InputTag("pfNewIsoPt02","gamma-DR030-ThresholdVeto000-ConeVeto001"),

    puppiNewIsoPt04_ch = cms.InputTag("puppiNewIsoPt04","h+-DR030-ThresholdVeto000-ConeVeto000"),
    puppiNewIsoPt04_nh = cms.InputTag("puppiNewIsoPt04","h0-DR030-ThresholdVeto000-ConeVeto001"),
    puppiNewIsoPt04_ph = cms.InputTag("puppiNewIsoPt04","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
    pfNewIsoPt04_ch = cms.InputTag("pfNewIsoPt04","h+-DR030-ThresholdVeto000-ConeVeto000"),
    pfNewIsoPt04_nh = cms.InputTag("pfNewIsoPt04","h0-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt04_ph = cms.InputTag("pfNewIsoPt04","gamma-DR030-ThresholdVeto000-ConeVeto001"),

    puppiNewIsoPt05_ch = cms.InputTag("puppiNewIsoPt05","h+-DR030-ThresholdVeto000-ConeVeto000"),
    puppiNewIsoPt05_nh = cms.InputTag("puppiNewIsoPt05","h0-DR030-ThresholdVeto000-ConeVeto001"),
    puppiNewIsoPt05_ph = cms.InputTag("puppiNewIsoPt05","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
    pfNewIsoPt05_ch = cms.InputTag("pfNewIsoPt05","h+-DR030-ThresholdVeto000-ConeVeto000"),
    pfNewIsoPt05_nh = cms.InputTag("pfNewIsoPt05","h0-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt05_ph = cms.InputTag("pfNewIsoPt05","gamma-DR030-ThresholdVeto000-ConeVeto001"),

    puppiNewIsoPt06_ch = cms.InputTag("puppiNewIsoPt06","h+-DR030-ThresholdVeto000-ConeVeto000"),
    puppiNewIsoPt06_nh = cms.InputTag("puppiNewIsoPt06","h0-DR030-ThresholdVeto000-ConeVeto001"),
    puppiNewIsoPt06_ph = cms.InputTag("puppiNewIsoPt06","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
    pfNewIsoPt06_ch = cms.InputTag("pfNewIsoPt06","h+-DR030-ThresholdVeto000-ConeVeto000"),
    pfNewIsoPt06_nh = cms.InputTag("pfNewIsoPt06","h0-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt06_ph = cms.InputTag("pfNewIsoPt06","gamma-DR030-ThresholdVeto000-ConeVeto001"),

    puppiNewIsoPt08_ch = cms.InputTag("puppiNewIsoPt08","h+-DR030-ThresholdVeto000-ConeVeto000"),
    puppiNewIsoPt08_nh = cms.InputTag("puppiNewIsoPt08","h0-DR030-ThresholdVeto000-ConeVeto001"),
    puppiNewIsoPt08_ph = cms.InputTag("puppiNewIsoPt08","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
    pfNewIsoPt08_ch = cms.InputTag("pfNewIsoPt08","h+-DR030-ThresholdVeto000-ConeVeto000"),
    pfNewIsoPt08_nh = cms.InputTag("pfNewIsoPt08","h0-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt08_ph = cms.InputTag("pfNewIsoPt08","gamma-DR030-ThresholdVeto000-ConeVeto001"),

    puppiNewIsoPt10_ch = cms.InputTag("puppiNewIsoPt10","h+-DR030-ThresholdVeto000-ConeVeto000"),
    puppiNewIsoPt10_nh = cms.InputTag("puppiNewIsoPt10","h0-DR030-ThresholdVeto000-ConeVeto001"),
    puppiNewIsoPt10_ph = cms.InputTag("puppiNewIsoPt10","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
    pfNewIsoPt10_ch = cms.InputTag("pfNewIsoPt10","h+-DR030-ThresholdVeto000-ConeVeto000"),
    pfNewIsoPt10_nh = cms.InputTag("pfNewIsoPt10","h0-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt10_ph = cms.InputTag("pfNewIsoPt10","gamma-DR030-ThresholdVeto000-ConeVeto001"),

    puppiNewIsoPt15_ch = cms.InputTag("puppiNewIsoPt15","h+-DR030-ThresholdVeto000-ConeVeto000"),
    puppiNewIsoPt15_nh = cms.InputTag("puppiNewIsoPt15","h0-DR030-ThresholdVeto000-ConeVeto001"),
    puppiNewIsoPt15_ph = cms.InputTag("puppiNewIsoPt15","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
    pfNewIsoPt15_ch = cms.InputTag("pfNewIsoPt15","h+-DR030-ThresholdVeto000-ConeVeto000"),
    pfNewIsoPt15_nh = cms.InputTag("pfNewIsoPt15","h0-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt15_ph = cms.InputTag("pfNewIsoPt15","gamma-DR030-ThresholdVeto000-ConeVeto001"),

    puppiNewIsoPt20_ch = cms.InputTag("puppiNewIsoPt20","h+-DR030-ThresholdVeto000-ConeVeto000"),
    puppiNewIsoPt20_nh = cms.InputTag("puppiNewIsoPt20","h0-DR030-ThresholdVeto000-ConeVeto001"),
    puppiNewIsoPt20_ph = cms.InputTag("puppiNewIsoPt20","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
    pfNewIsoPt20_ch = cms.InputTag("pfNewIsoPt20","h+-DR030-ThresholdVeto000-ConeVeto000"),
    pfNewIsoPt20_nh = cms.InputTag("pfNewIsoPt20","h0-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt20_ph = cms.InputTag("pfNewIsoPt20","gamma-DR030-ThresholdVeto000-ConeVeto001"),
"""
    
process.PatMuonAnalyser = cms.EDAnalyzer("PatMuonAnalyser",
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    addPileupInfo = cms.InputTag("slimmedAddPileupInfo"),
    muons = cms.InputTag("slimmedMuons"),
    pruned = cms.InputTag("prunedGenParticles"),
    
    puppiNewIso_ch = cms.InputTag("puppiNewIso","h+-DR030-ThresholdVeto000-ConeVeto000"),
    puppiNewIso_nh = cms.InputTag("puppiNewIso","h0-DR030-ThresholdVeto000-ConeVeto001"),
    puppiNewIso_ph = cms.InputTag("puppiNewIso","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
    trkNewIso = cms.InputTag("trkNewIso","h+-DR030-ThresholdVeto000-ConeVeto000"),
    pfNewIso_ch = cms.InputTag("pfNewIso","h+-DR030-ThresholdVeto000-ConeVeto000"),
    pfNewIso_nh = cms.InputTag("pfNewIso","h0-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIso_ph = cms.InputTag("pfNewIso","gamma-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIso_pu = cms.InputTag("pfNewIso","pu-DR030-ThresholdVeto000-ConeVeto000"),
    minipuppiNewIso_ch = cms.InputTag("minipuppiNewIso","h+-DR030-ThresholdVeto000-ConeVeto000"),
    minipuppiNewIso_nh = cms.InputTag("minipuppiNewIso","h0-DR030-ThresholdVeto000-ConeVeto001"),
    minipuppiNewIso_ph = cms.InputTag("minipuppiNewIso","gamma-DR030-ThresholdVeto000-ConeVeto001"),
    minitrkNewIso = cms.InputTag("minitrkNewIso","h+-DR030-ThresholdVeto000-ConeVeto000"),
    minipfNewIso_ch = cms.InputTag("minipfNewIso","h+-DR030-ThresholdVeto000-ConeVeto000"),
    minipfNewIso_nh = cms.InputTag("minipfNewIso","h0-DR030-ThresholdVeto000-ConeVeto001"),
    minipfNewIso_ph = cms.InputTag("minipfNewIso","gamma-DR030-ThresholdVeto000-ConeVeto001"),
    minipfNewIso_pu = cms.InputTag("minipfNewIso","pu-DR030-ThresholdVeto000-ConeVeto000"),
    
    puppiNewIsoPt02_ch = cms.InputTag("puppiNewIsoPt02","h+-DR030-ThresholdVeto000-ConeVeto000"),
    puppiNewIsoPt02_nh = cms.InputTag("puppiNewIsoPt02","h0-DR030-ThresholdVeto000-ConeVeto001"),
    puppiNewIsoPt02_ph = cms.InputTag("puppiNewIsoPt02","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
    pfNewIsoPt02_ch = cms.InputTag("pfNewIsoPt02","h+-DR030-ThresholdVeto000-ConeVeto000"),
    pfNewIsoPt02_nh = cms.InputTag("pfNewIsoPt02","h0-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt02_ph = cms.InputTag("pfNewIsoPt02","gamma-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt02_pu = cms.InputTag("pfNewIsoPt02","pu-DR030-ThresholdVeto000-ConeVeto000"),

    puppiNewIsoPt04_ch = cms.InputTag("puppiNewIsoPt04","h+-DR030-ThresholdVeto000-ConeVeto000"),
    puppiNewIsoPt04_nh = cms.InputTag("puppiNewIsoPt04","h0-DR030-ThresholdVeto000-ConeVeto001"),
    puppiNewIsoPt04_ph = cms.InputTag("puppiNewIsoPt04","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
    pfNewIsoPt04_ch = cms.InputTag("pfNewIsoPt04","h+-DR030-ThresholdVeto000-ConeVeto000"),
    pfNewIsoPt04_nh = cms.InputTag("pfNewIsoPt04","h0-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt04_ph = cms.InputTag("pfNewIsoPt04","gamma-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt04_pu = cms.InputTag("pfNewIsoPt04","pu-DR030-ThresholdVeto000-ConeVeto000"),

    puppiNewIsoPt05_ch = cms.InputTag("puppiNewIsoPt05","h+-DR030-ThresholdVeto000-ConeVeto000"),
    puppiNewIsoPt05_nh = cms.InputTag("puppiNewIsoPt05","h0-DR030-ThresholdVeto000-ConeVeto001"),
    puppiNewIsoPt05_ph = cms.InputTag("puppiNewIsoPt05","gamma-DR030-ThresholdVeto000-ConeVeto001"),    
    pfNewIsoPt05_ch = cms.InputTag("pfNewIsoPt05","h+-DR030-ThresholdVeto000-ConeVeto000"),
    pfNewIsoPt05_nh = cms.InputTag("pfNewIsoPt05","h0-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt05_ph = cms.InputTag("pfNewIsoPt05","gamma-DR030-ThresholdVeto000-ConeVeto001"),
    pfNewIsoPt05_pu = cms.InputTag("pfNewIsoPt05","pu-DR030-ThresholdVeto000-ConeVeto000"),
  )

process.p = cms.Path(
    process.puppiNewIso+process.trkNewIso+process.pfNewIso+
    process.minipuppiNewIso+process.minitrkNewIso+process.minipfNewIso+
    process.puppiNewIsoPt02+process.pfNewIsoPt02+
    process.puppiNewIsoPt04+process.pfNewIsoPt04+
    process.puppiNewIsoPt05+process.pfNewIsoPt05+
    #process.puppiNewIsoPt06+process.pfNewIsoPt06+
    #process.puppiNewIsoPt08+process.pfNewIsoPt08+
    #process.puppiNewIsoPt10+process.pfNewIsoPt10+
    #process.puppiNewIsoPt15+process.pfNewIsoPt15+
    #process.puppiNewIsoPt20+process.pfNewIsoPt20+
    process.PatMuonAnalyser)
