INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO post (author_id, created, w_elder, w_ancient, o_mithril, o_oric, c_silk, c_gossamer, l_rough, l_hardened, lucentmotes, reclaimedmetal, s_pain, s_enhance, s_control, c_skill, c_potency, c_brilliance, luck10, luck50, luck100, luck200, rare, exotic, r_salvaged, e_salvaged, r_ecto, e_ecto)
VALUES
  (1, '2018-01-01 00:00:00', 1805, 136, 1978, 208, 1667, 64, 1285, 75, 902, 4, 6, 4, 1, 4, 2, 2, 2000, 800, 106, 56, 163, 7, 0, 0, 0, 0)