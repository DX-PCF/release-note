HCP Terraformの導入をご検討いただきありがとうございます。
Google Cloud環境へのHCP Terraform導入計画について、調査結果をまとめたレポートを作成いたしました。アカウントの準備から基本的な使い方、大規模組織での高度な活用方法まで、導入プロセス全体を網羅的に解説しています。ぜひご活用ください。

---

## HCP Terraform 導入計画支援レポート

### 1. はじめに

HCP Terraformは、Infrastructure as Code (IaC) を実現するツール「Terraform」を、チームや組織で安全かつ効率的に利用するためにHashiCorpが提供するマネージドサービス（SaaS）です 。本レポートでは、HCP Terraformの導入を計画されている皆様に向けて、その基本的な概念からGoogle Cloud環境との具体的な連携手順、さらには大規模組織で活用するためのベストプラクティスまでを包括的に解説します。

### 2. HCP Terraformの基本

#### 2.1. HCP Terraformとは

HCP Terraform（旧称: Terraform Cloud）は、Terraformの実行環境、状態（State）ファイル管理、チームでの共同作業を支援する機能をクラウド上で提供するプラットフォームです [[1]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBplD6VkP549p709fmgw2JWrvr_hkggKzeFRkfN1ukZ9H2sSnx2KjvEKsUlFwJnwQ3_KUPGwgSmlRCa6UABsLX72NDe77KJ5heHFy-GZ1OEfjrlD2sIqEKbU2W4n2K2Y_y4WIGvwWoYto48mUsY7I=)[[2]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESQOBplYzB857hwpWvBWsJX_Z9bcp5_ycO1f80tRaKleFVnj_xIliRqwPnEzm7wTYFdNkNOQLByukYJBM52-uwpC5h5yctOE-TvoRKvyXZQHCokqBHmlz1qcwT6M1ZYeuwMsEk3hDUOJI-kQ5--A==)[[3]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELId1Q6sOXXv3ZaD8G2UGTFdtuuPf7PgNz6hbY0VzB8TOvjpDsSxuFaVt_-fVhXwFtFmxwIpd3sj_akdDS0kOrxwRTcVbmb_XFbU46tXTpYhM9deLGXu9oR1w-BOEh1L9yNwFaRxvriIxHbSEgA2k0WddO4jcdzl3LCBFJOGm9UvLwEj-vFD6KJeVzj8a-c6qZ40uSxM7DQsLutQE=) 。開発者や運用チームは、ローカル環境の差異を気にすることなく、一貫性のある信頼性の高い環境でインフラのプロビジョニングを自動化できます [[1]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBplD6VkP549p709fmgw2JWrvr_hkggKzeFRkfN1ukZ9H2sSnx2KjvEKsUlFwJnwQ3_KUPGwgSmlRCa6UABsLX72NDe77KJ5heHFy-GZ1OEfjrlD2sIqEKbU2W4n2K2Y_y4WIGvwWoYto48mUsY7I=) 。

#### 2.2. 主な機能

HCP Terraformは、オープンソース版の機能に加え、組織での利用を促進するための多くの機能を提供します。

*   **リモート状態管理 (Remote State Management)**: Terraformの状態ファイル（tfstate）を安全に一元管理し、チーム内での共有と変更時のロックを自動で行います [[4]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuXJznQVJkaDYQwVN7ROhmA4mLXynUIca-hdrY5_KCKpJ1szA4QE07Ykb99U_nTZaygLPR3M5uFIUZ_8A5jzk5E9kVFwlFdMfghrfmEl5MSJ2aK6ZRTiI8v4TeNycftmWH48xHi2Up9TNBB9K2RzArH0gQgddxuLV7ClVasbJYdXGJIw_s9g==)[[2]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESQOBplYzB857hwpWvBWsJX_Z9bcp5_ycO1f80tRaKleFVnj_xIliRqwPnEzm7wTYFdNkNOQLByukYJBM52-uwpC5h5yctOE-TvoRKvyXZQHCokqBHmlz1qcwT6M1ZYeuwMsEk3hDUOJI-kQ5--A==)[[5]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBcjPzmO8CRoWxcitH1PLFs--AQd7BRm4FqApJu_MzNK6o6-ImykBCPjOjJcudGICBhW6t9Zog_WQjGNah5PClk2wCbMyIPKqhrXrEcTJneja_FC9BQpUK-3id2vKGoe8W19YG) 。
*   **バージョン管理システム (VCS) との連携**: GitHubやGitLabなどと連携し、コードの変更をトリガーにTerraformの実行（plan/apply）を自動化するCI/CDパイプラインを容易に構築できます [[4]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuXJznQVJkaDYQwVN7ROhmA4mLXynUIca-hdrY5_KCKpJ1szA4QE07Ykb99U_nTZaygLPR3M5uFIUZ_8A5jzk5E9kVFwlFdMfghrfmEl5MSJ2aK6ZRTiI8v4TeNycftmWH48xHi2Up9TNBB9K2RzArH0gQgddxuLV7ClVasbJYdXGJIw_s9g==)[[2]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESQOBplYzB857hwpWvBWsJX_Z9bcp5_ycO1f80tRaKleFVnj_xIliRqwPnEzm7wTYFdNkNOQLByukYJBM52-uwpC5h5yctOE-TvoRKvyXZQHCokqBHmlz1qcwT6M1ZYeuwMsEk3hDUOJI-kQ5--A==)[[6]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_V_r2OcTKjH4Cdwlk0L5pFnxwb89yQCrcb5nwn_4J_pxsn4WFJ0o-3M9DmVx5fJcB782mn9cmON2cXYQDP1W5F-vAaMYj8hSlsZ4L3BiwxT5s6g6mnSDKcflvgQrGRMQRl78AApfj0yaqH49yuDzMu8z5gW27JjbSYf-21BgN_JO20Fg=) 。
*   **ワークスペース (Workspaces)**: 開発、ステージング、本番といった環境ごとに状態ファイルや変数を分離して管理できます [[7]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDSg55g3ebOWvKu7J4gEIkMCfOxZc90PUOldOao22xzrsnMg-ay8paxF-jBp3Zraaq9EVC-fwAgrT7WOjmC7DfsSWn7vL5yLNDFxRGYua6daSFUmRmiDhT_1psIshSWM9HkcPKnA==)[[2]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESQOBplYzB857hwpWvBWsJX_Z9bcp5_ycO1f80tRaKleFVnj_xIliRqwPnEzm7wTYFdNkNOQLByukYJBM52-uwpC5h5yctOE-TvoRKvyXZQHCokqBHmlz1qcwT6M1ZYeuwMsEk3hDUOJI-kQ5--A==) 。
*   **ポリシー・アズ・コード (Policy as Code)**: SentinelやOpen Policy Agent (OPA) を用い、組織のセキュリティポリシーやコストに関するルールをコード化し、インフラ変更前に自動でチェックできます [[4]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuXJznQVJkaDYQwVN7ROhmA4mLXynUIca-hdrY5_KCKpJ1szA4QE07Ykb99U_nTZaygLPR3M5uFIUZ_8A5jzk5E9kVFwlFdMfghrfmEl5MSJ2aK6ZRTiI8v4TeNycftmWH48xHi2Up9TNBB9K2RzArH0gQgddxuLV7ClVasbJYdXGJIw_s9g==)[[5]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBcjPzmO8CRoWxcitH1PLFs--AQd7BRm4FqApJu_MzNK6o6-ImykBCPjOjJcudGICBhW6t9Zog_WQjGNah5PClk2wCbMyIPKqhrXrEcTJneja_FC9BQpUK-3id2vKGoe8W19YG)[[8]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdB5tcOgNc54Mz2QgJANLmMWOMGLdV0vIPpJafXT1zNn_kYq19fhljjrqKYpU1bhDfTqXomgZs92uMhJSmvlKSv7rL-tQsPIkE03v8REntMTgFfWB3CYqIL_h9szjAubpwmSQlbBfDtcC9tonb06fcSDmLOM_6MFDUhSOuEtadF02Nsw==) 。
*   **プライベートレジストリ (Private Registry)**: 組織内で再利用したいTerraformモジュールやプロバイダを安全に共有できます [[4]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuXJznQVJkaDYQwVN7ROhmA4mLXynUIca-hdrY5_KCKpJ1szA4QE07Ykb99U_nTZaygLPR3M5uFIUZ_8A5jzk5E9kVFwlFdMfghrfmEl5MSJ2aK6ZRTiI8v4TeNycftmWH48xHi2Up9TNBB9K2RzArH0gQgddxuLV7ClVasbJYdXGJIw_s9g==)[[9]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4X5ZlVU4c7X6b2CryDNMt2URvOkGpowjYL8vq7ehUsjsfJ4GZXARC6aKJ1SG9dh2M7G_-9pGr_zmpXdToyqrBEyPcuOtj4KvsMSEViVASeonVr9Bb1aYHrFZbTU6YM9knEF2TUQe5sQ-lLtaAKq989YTmPxYobCEGO95foybtZeg_n-SnPBT6mRYZ3Q==) 。
*   **コスト見積もり (Cost Estimation)**: 構成変更によって発生するコストの増減を、適用前に予測・表示します [[10]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOkT9HvyePj1G4_ueOoyGVIm93-y7a4jrRL5EYnmm2JcIEbJMkOayO752Wiq3jZeq60ipewtJKceD7LHBnU2S3O-qAUWDKe606EexqzFaCqd5o_SK9QLpreuffEDRk45lN3Q7F4XF288z56FS3B-9ZK-VqsUkXXBehmOhLS7yCbBTbWVug7kJxPYrV1utjXUPmACaQzMpl417dGL7dlvbG89GCP_wweej2cjGcJebxIX8uTCCmssQ=)[[9]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4X5ZlVU4c7X6b2CryDNMt2URvOkGpowjYL8vq7ehUsjsfJ4GZXARC6aKJ1SG9dh2M7G_-9pGr_zmpXdToyqrBEyPcuOtj4KvsMSEViVASeonVr9Bb1aYHrFZbTU6YM9knEF2TUQe5sQ-lLtaAKq989YTmPxYobCEGO95foybtZeg_n-SnPBT6mRYZ3Q==) 。
*   **アクセス制御と監査ログ**: チームやメンバーごとに詳細な権限設定が可能で、操作履歴を記録する監査ログ機能も提供されます [[10]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOkT9HvyePj1G4_ueOoyGVIm93-y7a4jrRL5EYnmm2JcIEbJMkOayO752Wiq3jZeq60ipewtJKceD7LHBnU2S3O-qAUWDKe606EexqzFaCqd5o_SK9QLpreuffEDRk45lN3Q7F4XF288z56FS3B-9ZK-VqsUkXXBehmOhLS7yCbBTbWVug7kJxPYrV1utjXUPmACaQzMpl417dGL7dlvbG89GCP_wweej2cjGcJebxIX8uTCCmssQ=)[[5]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBcjPzmO8CRoWxcitH1PLFs--AQd7BRm4FqApJu_MzNK6o6-ImykBCPjOjJcudGICBhW6t9Zog_WQjGNah5PClk2wCbMyIPKqhrXrEcTJneja_FC9BQpUK-3id2vKGoe8W19YG) 。
*   **セキュアな変数管理**: APIキーなどの機密情報を暗号化して安全に保管できます [[11]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaxqP8fbORDEvNnmTzC32dnwTgnHDtwX-ecluVQPCGQ-rsDc6bqtKrLHKTif_2mZiug2LAr-IJ4bnHuiB5kHfAuAMpXGvLP318jInMasphOAmLPCJVU-2ogYm2wAdAyftvTUiwV3Vu-BKal51lHopaNVTkyiZIgTuROk53ywrhgusQKvloUyRQ) 。

#### 2.3. オープンソース版との違い

HCP Terraformは、個人利用を想定したオープンソース版が抱えるチーム開発での課題を解決します [[4]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuXJznQVJkaDYQwVN7ROhmA4mLXynUIca-hdrY5_KCKpJ1szA4QE07Ykb99U_nTZaygLPR3M5uFIUZ_8A5jzk5E9kVFwlFdMfghrfmEl5MSJ2aK6ZRTiI8v4TeNycftmWH48xHi2Up9TNBB9K2RzArH0gQgddxuLV7ClVasbJYdXGJIw_s9g==) 。

| 機能 | HCP Terraform (SaaS) | Terraform (オープンソース版) |
| :--- | :--- | :--- |
| **実行環境** | HashiCorpが管理するクラウド環境 | ユーザーのローカルマシンやCI/CDサーバー |
| **UI** | WebベースのGUIを提供  | CUI (コマンドライン) のみ [[12]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErD5TkczEbVQnv3Mhc0ogZqrEjajPC159iGamLcHuISNsYN27bzC6rxd5M9vDhtdWeMgfFRqGfBjR78wK4PcdosqbE8JS4iC5URRl1P6ll6YM4gEA2PlAyfzqjSNj0HBkLp0Ztopp5z_-Ph-S-fqgrhjUCsI-7A84e2Jb0pAMM_IuocGKLCb3BZZtECaXZz1k=)  |
| **状態管理** | 自動で状態ファイルを管理・共有・ロック [[4]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuXJznQVJkaDYQwVN7ROhmA4mLXynUIca-hdrY5_KCKpJ1szA4QE07Ykb99U_nTZaygLPR3M5uFIUZ_8A5jzk5E9kVFwlFdMfghrfmEl5MSJ2aK6ZRTiI8v4TeNycftmWH48xHi2Up9TNBB9K2RzArH0gQgddxuLV7ClVasbJYdXGJIw_s9g==)[[2]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESQOBplYzB857hwpWvBWsJX_Z9bcp5_ycO1f80tRaKleFVnj_xIliRqwPnEzm7wTYFdNkNOQLByukYJBM52-uwpC5h5yctOE-TvoRKvyXZQHCokqBHmlz1qcwT6M1ZYeuwMsEk3hDUOJI-kQ5--A==)  | ユーザー自身でGCSバケット等を用意し管理する必要がある [[4]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuXJznQVJkaDYQwVN7ROhmA4mLXynUIca-hdrY5_KCKpJ1szA4QE07Ykb99U_nTZaygLPR3M5uFIUZ_8A5jzk5E9kVFwlFdMfghrfmEl5MSJ2aK6ZRTiI8v4TeNycftmWH48xHi2Up9TNBB9K2RzArH0gQgddxuLV7ClVasbJYdXGJIw_s9g==)  |
| **共同作業** | チーム管理、アクセス制御、承認ワークフローを標準提供 [[6]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_V_r2OcTKjH4Cdwlk0L5pFnxwb89yQCrcb5nwn_4J_pxsn4WFJ0o-3M9DmVx5fJcB782mn9cmON2cXYQDP1W5F-vAaMYj8hSlsZ4L3BiwxT5s6g6mnSDKcflvgQrGRMQRl78AApfj0yaqH49yuDzMu8z5gW27JjbSYf-21BgN_JO20Fg=)[[12]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErD5TkczEbVQnv3Mhc0ogZqrEjajPC159iGamLcHuISNsYN27bzC6rxd5M9vDhtdWeMgfFRqGfBjR78wK4PcdosqbE8JS4iC5URRl1P6ll6YM4gEA2PlAyfzqjSNj0HBkLp0Ztopp5z_-Ph-S-fqgrhjUCsI-7A84e2Jb0pAMM_IuocGKLCb3BZZtECaXZz1k=)  | Gitフローなどの運用ルールでカバーする必要がある |
| **ガバナンス** | ポリシー・アズ・コード、コスト見積もり、監査ログ [[4]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuXJznQVJkaDYQwVN7ROhmA4mLXynUIca-hdrY5_KCKpJ1szA4QE07Ykb99U_nTZaygLPR3M5uFIUZ_8A5jzk5E9kVFwlFdMfghrfmEl5MSJ2aK6ZRTiI8v4TeNycftmWH48xHi2Up9TNBB9K2RzArH0gQgddxuLV7ClVasbJYdXGJIw_s9g==)[[9]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4X5ZlVU4c7X6b2CryDNMt2URvOkGpowjYL8vq7ehUsjsfJ4GZXARC6aKJ1SG9dh2M7G_-9pGr_zmpXdToyqrBEyPcuOtj4KvsMSEViVASeonVr9Bb1aYHrFZbTU6YM9knEF2TUQe5sQ-lLtaAKq989YTmPxYobCEGO95foybtZeg_n-SnPBT6mRYZ3Q==)[[5]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBcjPzmO8CRoWxcitH1PLFs--AQd7BRm4FqApJu_MzNK6o6-ImykBCPjOjJcudGICBhW6t9Zog_WQjGNah5PClk2wCbMyIPKqhrXrEcTJneja_FC9BQpUK-3id2vKGoe8W19YG)  | なし |
| **CI/CD** | VCS連携により容易に構築可能 [[6]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_V_r2OcTKjH4Cdwlk0L5pFnxwb89yQCrcb5nwn_4J_pxsn4WFJ0o-3M9DmVx5fJcB782mn9cmON2cXYQDP1W5F-vAaMYj8hSlsZ4L3BiwxT5s6g6mnSDKcflvgQrGRMQRl78AApfj0yaqH49yuDzMu8z5gW27JjbSYf-21BgN_JO20Fg=)  | GitHub Actionsなどで自前で作り込む必要がある [[4]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuXJznQVJkaDYQwVN7ROhmA4mLXynUIca-hdrY5_KCKpJ1szA4QE07Ykb99U_nTZaygLPR3M5uFIUZ_8A5jzk5E9kVFwlFdMfghrfmEl5MSJ2aK6ZRTiI8v4TeNycftmWH48xHi2Up9TNBB9K2RzArH0gQgddxuLV7ClVasbJYdXGJIw_s9g==)  |

#### 2.4. 料金プランと機能

HCP Terraformの料金は、2023年6月にユーザー数ベースから「管理下のリソース数（Resources Under Management - RUM）」に応じた課金体系に変更されました [[13]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFWzO7WRFetQ863xuIYT8wmRkIARMmlaN7UkfnYyy_zFhdg2RtHP4nwDTiJn8a0DE_leZbFrWi1DZHGPhaOc0xODPevu5SQbjpb2t05AZHsBjITZgDsW2uvQqKxtyGDbsQ4sMbeaezOpyk0vjFtr7OPzA=)[[14]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwXA6hlU2_HS-Pa0HYEtKF45r3KRtwxAzdi4nLiOrTdB5sjwwbK0exDi_WEZ4cpPTZTABTBuIMCWoiNK0ee7Vg4ZJx3HNJfQ5tMROhF7AidUmzaCf9TIll6EZ324twRBbC8hFqzlmDNrx3oXk=) 。これにより、利用規模に応じた柔軟なコスト管理が可能になっています。料金プランはOrganization（組織）単位で選択し、プランごとに利用できる機能が異なります [[15]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzlEitzC1TysSW_BRNGHX0-weXyQ9QcQyp_fHQ73Skjml25V6J_KTFPhsmnZH66oAd4rcemNNMO6HRFdYSFg0LjJl0Xx3yRdouLHJSYxpnf77E3v0flKXUsr7SAg3ce3JnokOycZSvxbY6lg6BwpNqS7GB8gNTfNU=)[[11]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaxqP8fbORDEvNnmTzC32dnwTgnHDtwX-ecluVQPCGQ-rsDc6bqtKrLHKTif_2mZiug2LAr-IJ4bnHuiB5kHfAuAMpXGvLP318jInMasphOAmLPCJVU-2ogYm2wAdAyftvTUiwV3Vu-BKal51lHopaNVTkyiZIgTuROk53ywrhgusQKvloUyRQ) 。導入計画時には、利用したい機能を特定し、対応するプランを選択することが重要です。

| プラン | 主な対象 | コスト体系 | 主な機能 |
| :--- | :--- | :--- | :--- |
| **Free** | 個人、小規模チームの学習・評価 | 無料 | ・管理リソース数: 500まで<br>・同時実行数: 1<br>・リモート状態管理<br>・VCS連携<br>・プライベートレジストリ<br>・ポリシー適用（制限あり） [[10]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOkT9HvyePj1G4_ueOoyGVIm93-y7a4jrRL5EYnmm2JcIEbJMkOayO752Wiq3jZeq60ipewtJKceD7LHBnU2S3O-qAUWDKe606EexqzFaCqd5o_SK9QLpreuffEDRk45lN3Q7F4XF288z56FS3B-9ZK-VqsUkXXBehmOhLS7yCbBTbWVug7kJxPYrV1utjXUPmACaQzMpl417dGL7dlvbG89GCP_wweej2cjGcJebxIX8uTCCmssQ=)[[15]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzlEitzC1TysSW_BRNGHX0-weXyQ9QcQyp_fHQ73Skjml25V6J_KTFPhsmnZH66oAd4rcemNNMO6HRFdYSFg0LjJl0Xx3yRdouLHJSYxpnf77E3v0flKXUsr7SAg3ce3JnokOycZSvxbY6lg6BwpNqS7GB8gNTfNU=)[[13]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFWzO7WRFetQ863xuIYT8wmRkIARMmlaN7UkfnYyy_zFhdg2RtHP4nwDTiJn8a0DE_leZbFrWi1DZHGPhaOc0xODPevu5SQbjpb2t05AZHsBjITZgDsW2uvQqKxtyGDbsQ4sMbeaezOpyk0vjFtr7OPzA=)[[8]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdB5tcOgNc54Mz2QgJANLmMWOMGLdV0vIPpJafXT1zNn_kYq19fhljjrqKYpU1bhDfTqXomgZs92uMhJSmvlKSv7rL-tQsPIkE03v8REntMTgFfWB3CYqIL_h9szjAubpwmSQlbBfDtcC9tonb06fcSDmLOM_6MFDUhSOuEtadF02Nsw==)  |
| **Standard** | インフラ自動化を標準化するチーム | 501リソース以上から従量課金（$0.00014/時/リソース） [[13]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFWzO7WRFetQ863xuIYT8wmRkIARMmlaN7UkfnYyy_zFhdg2RtHP4nwDTiJn8a0DE_leZbFrWi1DZHGPhaOc0xODPevu5SQbjpb2t05AZHsBjITZgDsW2uvQqKxtyGDbsQ4sMbeaezOpyk0vjFtr7OPzA=)[[14]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwXA6hlU2_HS-Pa0HYEtKF45r3KRtwxAzdi4nLiOrTdB5sjwwbK0exDi_WEZ4cpPTZTABTBuIMCWoiNK0ee7Vg4ZJx3HNJfQ5tMROhF7AidUmzaCf9TIll6EZ324twRBbC8hFqzlmDNrx3oXk=)  | Freeプランの全機能に加え、<br>・管理リソース数の上限なし<br>・同時実行数: 3<br>・**チーム管理機能**<br>・**コスト見積もり (Cost Estimation)**<br>・**Policy as Code (Sentinel/OPA)** [[10]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOkT9HvyePj1G4_ueOoyGVIm93-y7a4jrRL5EYnmm2JcIEbJMkOayO752Wiq3jZeq60ipewtJKceD7LHBnU2S3O-qAUWDKe606EexqzFaCqd5o_SK9QLpreuffEDRk45lN3Q7F4XF288z56FS3B-9ZK-VqsUkXXBehmOhLS7yCbBTbWVug7kJxPYrV1utjXUPmACaQzMpl417dGL7dlvbG89GCP_wweej2cjGcJebxIX8uTCCmssQ=)[[13]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFWzO7WRFetQ863xuIYT8wmRkIARMmlaN7UkfnYyy_zFhdg2RtHP4nwDTiJn8a0DE_leZbFrWi1DZHGPhaOc0xODPevu5SQbjpb2t05AZHsBjITZgDsW2uvQqKxtyGDbsQ4sMbeaezOpyk0vjFtr7OPzA=)  |
| **Plus** | 運用可視性とガバナンスを強化したい組織 | 年間契約（要問い合わせ） [[13]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFWzO7WRFetQ863xuIYT8wmRkIARMmlaN7UkfnYyy_zFhdg2RtHP4nwDTiJn8a0DE_leZbFrWi1DZHGPhaOc0xODPevu5SQbjpb2t05AZHsBjITZgDsW2uvQqKxtyGDbsQ4sMbeaezOpyk0vjFtr7OPzA=)  | Standardプランの全機能に加え、<br>・**監査ログ (Audit Logging)**<br>・**ドリフト検出 (Drift Detection)**<br>・**継続的検証 (Continuous Validation)**<br>・**エージェントによるセルフホスト実行**<br>・高度なチーム管理ツール [[10]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOkT9HvyePj1G4_ueOoyGVIm93-y7a4jrRL5EYnmm2JcIEbJMkOayO752Wiq3jZeq60ipewtJKceD7LHBnU2S3O-qAUWDKe606EexqzFaCqd5o_SK9QLpreuffEDRk45lN3Q7F4XF288z56FS3B-9ZK-VqsUkXXBehmOhLS7yCbBTbWVug7kJxPYrV1utjXUPmACaQzMpl417dGL7dlvbG89GCP_wweej2cjGcJebxIX8uTCCmssQ=)  |
| **Premium** | 高度なセキュリティとコンプライアンスが求められる大企業 | 年間契約（要問い合わせ） | Plusプランの全機能に加え、<br>・高度なセキュリティ機能（SSOなど）<br>・コンプライアンス機能<br>・専任サポート [[10]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOkT9HvyePj1G4_ueOoyGVIm93-y7a4jrRL5EYnmm2JcIEbJMkOayO752Wiq3jZeq60ipewtJKceD7LHBnU2S3O-qAUWDKe606EexqzFaCqd5o_SK9QLpreuffEDRk45lN3Q7F4XF288z56FS3B-9ZK-VqsUkXXBehmOhLS7yCbBTbWVug7kJxPYrV1utjXUPmACaQzMpl417dGL7dlvbG89GCP_wweej2cjGcJebxIX8uTCCmssQ=)[[16]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5pwSZXXjrATfyXzE0l-BLFKYmP8ULtW4drvQ-nFP4jfPIJDWyKaBRICROGPOeC5Ef1zN--8PmipnnH9IAtNWjxiFhe328PKQaXeoPN6T13SkIxyXYNUOACIfMcdFJpw==)  |

**注意**: 上記のコストは参考情報であり、正確な価格は公式サイトで確認する必要があります。

#### 2.5. Google Cloud環境で利用するメリット

*   **Google Cloudリソースの一元管理**: Compute Engine、Cloud Storage、IAMポリシーといったGoogle Cloudの様々なリソースを、他のクラウドサービスとともに単一のワークフローで管理できます [[17]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaJfAh8YCKL1SuEXREFu5UbZuOojNTLMK7pV7YZ1p_LPcUUQ-iazQBj88OD8MkEf4wh4N8xUSpf0_YvFfmqDtXusQdudHiK5xwU_Gv1BHXEd0jZYtieKIaXiiRlLTv4CwAXVeoPEwltUqUB6I=)[[18]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQDy5_QAvSa9mgnlDdQVH6EB6KV_KkUp6UChh3lhZYfTOc5Y356fjTQb6uaXYjzt-pfzsFs-kx1nCG_lJElYzb0y9qoM0FKKSg504PcAQrWjAExZo6lasA4W1B_FXff9l1jQnzq2UfMR5cAHHuGA6T5NxNBPQKaDo=) 。
*   **セキュアな認証連携 (OIDC)**: OpenID Connect (OIDC) を利用してHCP TerraformとGoogle Cloudを連携させることで、有効期間の長いサービスアカウントキーを管理することなく、安全に認証を行えます [[6]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_V_r2OcTKjH4Cdwlk0L5pFnxwb89yQCrcb5nwn_4J_pxsn4WFJ0o-3M9DmVx5fJcB782mn9cmON2cXYQDP1W5F-vAaMYj8hSlsZ4L3BiwxT5s6g6mnSDKcflvgQrGRMQRl78AApfj0yaqH49yuDzMu8z5gW27JjbSYf-21BgN_JO20Fg=) 。
*   **Googleとのパートナーシップ**: GoogleとHashiCorpはTerraformのGoogle Cloud Providerを共同で開発しており、GCPの新サービスにも迅速に対応します [[18]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQDy5_QAvSa9mgnlDdQVH6EB6KV_KkUp6UChh3lhZYfTOc5Y356fjTQb6uaXYjzt-pfzsFs-kx1nCG_lJElYzb0y9qoM0FKKSg504PcAQrWjAExZo6lasA4W1B_FXff9l1jQnzq2UfMR5cAHHuGA6T5NxNBPQKaDo=)[[19]](https://drive.google.com/a/vorn.co.jp/open?id=1u9-9IZOjfTiOfoWSVJK9x53CcD6MeXEt) 。
*   **共同サポート体制**: 問題発生時に両社のサポートチームが連携して対応するシームレスなサポートプロセスを利用できます [[20]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT-gVDe8-NRkHbyHH554tj_eixTQ5kRkMhuTPDdxeK5kuzAjQfAsqVCLtx6KFtwX7wQ_JKyBfCae6Fyu3S6zMDFFo8gfVwJAkDvVT0gMIrpaE4-yKe2vJWMpjyXUzzfloCIu5_w0IKLZNcMqxJkKde1OJbfLB3is2lopM12ezZG5VTbohgrW8tKf1P20oEmjXlKaoIZSFb9Rfm-KT6WkzO0nRBWXY1kamnwiTE82kf6zbQlvMpwUV0YUq-5SLYD1L13DkQ) 。

### 3. 導入に向けた具体的なステップ

#### 3.1. HCP Terraformの準備

1.  **アカウント作成**: [HCP Terraformのサインアップページ](https://app.terraform.io/public/signup/account)からアカウントを作成します [[21]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWe_QPn9glexmkgiNa63sPSIEUgAZSeLy9LkyHJVIpaMLzObK2G2fjxV4JL3Nl_g4jtemqGvhcf3YVOnDKGehYc2l1ALE5sR6UGcK1KiXyX7b23gW0nONh6bPV0qhbWcJ_YjAe-w_gkiwhYcTx3Oe6gG2X6IrE-CTnURh1oPd8PndsXiYPvwmX3KWNQUEYmkM=) 。
2.  **Organizationの作成**: アカウント作成後、チームでリソースを共有・管理するためのOrganization（組織）を作成します [[21]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWe_QPn9glexmkgiNa63sPSIEUgAZSeLy9LkyHJVIpaMLzObK2G2fjxV4JL3Nl_g4jtemqGvhcf3YVOnDKGehYc2l1ALE5sR6UGcK1KiXyX7b23gW0nONh6bPV0qhbWcJ_YjAe-w_gkiwhYcTx3Oe6gG2X6IrE-CTnURh1oPd8PndsXiYPvwmX3KWNQUEYmkM=)[[22]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqTvXlXJekUnS6xpXwbx1YALDcWOL0cDuaR35GNSt4S4_K7idCVem3ER-GGRthTDHWGzN_qf4-wYy7h0ROmQ_Cu2zV4ufCboXKtyLsdbPL0ozqEZ92sp7tDY-VcSyOnIWxKotOlwZs71AMEP9LzFQtOwoQ)[[23]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJzB_-DKqAZFFCsPG1Q6v7pzi2wLKcTAYNhEAmvOXDMHWMAy8zmqvqqPf5oyg9iLeV00YidLMXmjLgyXIb6SDalpglorHCnKKIn-WTUuo78HV4OVFyJBArRBIzsCkSC2uNAYmZhMxkkUPAfouaBUMYJb61KrOggbFI) 。
3.  **Workspaceの作成**: Organization内にプロジェクトを作成し、その中にTerraformの実行環境となるWorkspaceを作成します [[24]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEneaYAOPtz9KOMvKkVevjZe1kLm5pu7NDJhvHXxTgSZ6rRBBInHBT2e3ncyGu2rXROo_iuVF_SxzYkXj0v5PkdSBEus7PoqJW418SoxHvPP6SI7xRHFqlfuxDnl5v5Q_hfLdPkGw==)[[25]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCGBrlaF_KsYac3Fk5rhKr-zXAFTD0-jyb0g9GpsAGI58Lwad628O0H0ywrEGcMnP4g7Kj6sx736uyaNVOGb2EA6cJ4IFBtYtHZpY-dykkAZqwSOtO_Aqimw2M1GRqGoPry2NcjWHg-bJcCK0U8hc=) 。

#### 3.2. Google Cloudとの連携設定

HCP TerraformがGoogle Cloudリソースを操作できるよう、認証を設定します。

1.  **サービスアカウントの作成とIAMロールの設定**:
    *   Google Cloudコンソールの「IAMと管理」>「サービスアカウント」で、HCP Terraformが使用するサービスアカウントを作成します [[26]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGisTfIVCKvujWwiRLNpbGgBxqQx6CAPvLW0LEYt6s5eHa8vbbXwSLQzGhlbgvx6T6Fo36s64-KK0OUWtzs-7iS5qiTiaW4v5JCNtCL30AhY93hwf9-XmeF34BNAQ3hjFdp6R-5IMy35zqgcQ==) 。
    *   作成したサービスアカウントに対し、Terraformで管理したいリソースに応じたIAMロール（例: `roles/editor`）を付与します [[27]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM5XKZXp_AJPZnc1hJXk_bgCHCiBO3ffbaYuJuZkCrcwHWfxv3MnUiLKBONSiWf7Hz2A6eMlAUpsJp47IHy5IH5qqfFo5l7AW3HSHNixjBR8PtCwLQpeHwd0wizZDs_sBcZ0ysCG_XXCgv_YWIy5-Z-N3Q1_y7Scl2cxvmL2QO8Qiq1kImQ6aI28Y=) 。

2.  **認証方法の選択**:
    セキュリティ上、キーの漏洩リスクやローテーション管理が不要な**OIDC連携（動的クレデンシャル）が強く推奨されます** [[28]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEu1_yacb2RhcG_BDJwfocG9CQTkWG0XfwQgsWmsGrDr6W-ABp-DvhaezlNgX9bBT2TRSFOb2A3AKMEUQv5qBS7ElYjRHC7TxXUfKfuWCXxSH49kIltym3nhk4f9D2tBr5CMtBiptsV8FSPnj0ad8txFNU9BL1dTPVqS-aBIZWUegLNPNwtU4UCfzFPVoSQGSyQ5jb21vnPjYMDcHAOrqFgPJE8J1yX1SqC)[[22]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqTvXlXJekUnS6xpXwbx1YALDcWOL0cDuaR35GNSt4S4_K7idCVem3ER-GGRthTDHWGzN_qf4-wYy7h0ROmQ_Cu2zV4ufCboXKtyLsdbPL0ozqEZ92sp7tDY-VcSyOnIWxKotOlwZs71AMEP9LzFQtOwoQ) 。

    *   **方法A: 認証情報ファイル（JSONキー）**: サービスアカウントのJSONキーをダウンロードし、その内容をHCP TerraformのWorkspace変数 `GOOGLE_CREDENTIALS` に機密情報（Sensitive）として設定します [[29]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqOnsBLirK0QaOZqFkrzUJxHznC9V_d9QYmv46n75-qzETA5lGib9f3_TgvZ_q_eehAnyMzULZvHwGXfE9flkVM6qP7DiWbjW3fczipjkmYJWt-yEr6ICA00ZELETsd0V6M3qqAyttNn7xMN4y_cVbSiGMCdb8n9uC8BkgNVJnG3LDoSoxsVuQxicsX7J21ZJ5Oj3DLynmuHqZ6c5rNsyjZ2VJTGAIi9TU2J05V0hyVQwHmO5mV2xehXmt2KmKwbFLkciqXUtoKlViD_dNhW9m7w1eexKIhNDqqTxINS1Ib_j8fNdCrc5aYiWyQYMHn76eiyBIttTesZ9gCz4UxC3v87qKVPUPB1-sx3iMlSb3b8Tr1LVbbL-roJklB4weQQ6BJPU3jE0MAeb3QXR7-O1d3500P7PLWe5SX73dUmfE54HKOhAw1g==)[[22]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqTvXlXJekUnS6xpXwbx1YALDcWOL0cDuaR35GNSt4S4_K7idCVem3ER-GGRthTDHWGzN_qf4-wYy7h0ROmQ_Cu2zV4ufCboXKtyLsdbPL0ozqEZ92sp7tDY-VcSyOnIWxKotOlwZs71AMEP9LzFQtOwoQ) 。
    *   **方法B: OIDC連携（推奨）**: Google CloudのWorkload Identity連携機能を利用し、HCP TerraformとGoogle Cloud間で信頼関係を構築します。これにより、Terraformの実行ごとに短期的な認証情報が動的に発行されます [[30]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGbfIil9Ij24qV8wfLLTA9VVCVZwxwLm_X-D6oPc4upwtoEUcPw6204K66wTP-Ifbn4VokbbcNrDv8SUtCcJoq41dPn71jvoucnH0mSV2CG1pvfYdq6fL7DbdwToAKXBfAppObBoIPJUQJXKUFoew0trAe1sqIPTehIGQrqDf_h5MLTagX67Oh5Pou4w_T)[[31]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOGYw80uLzh12WAi4511CjwIwA0SKW61LqDv9pQHO5VAzvApLPGoQhm76Ne9GfRj1YwvSvOyyVYnZWTU7wH5geuS8eQi1tU-Tcm0LHK9RaX4CtYVAkwIJJu9kWQ5WYhFxDrtx78iUtTCkucP5A6ZpDHMcG1YfWRyYlcqr2qEdr8qd_hlkf8Wez8IahoZykfah7gJ7k23cv0DyvBIBrvc3GOFGtAwcrDKy_1AZRSA==) 。

3.  **OIDC連携（Workload Identity連携）の具体的な設定手順**:
    1.  **Google Cloud側**:
        *   「IAM and Admin API」と「Security Token Service API」を有効化します。
        *   「Workload Identity連携」でプールを作成し、プロバイダーを追加します。発行元URLには `https://app.terraform.io` を設定します [[28]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEu1_yacb2RhcG_BDJwfocG9CQTkWG0XfwQgsWmsGrDr6W-ABp-DvhaezlNgX9bBT2TRSFOb2A3AKMEUQv5qBS7ElYjRHC7TxXUfKfuWCXxSH49kIltym3nhk4f9D2tBr5CMtBiptsV8FSPnj0ad8txFNU9BL1dTPVqS-aBIZWUegLNPNwtU4UCfzFPVoSQGSyQ5jb21vnPjYMDcHAOrqFgPJE8J1yX1SqC)[[22]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqTvXlXJekUnS6xpXwbx1YALDcWOL0cDuaR35GNSt4S4_K7idCVem3ER-GGRthTDHWGzN_qf4-wYy7h0ROmQ_Cu2zV4ufCboXKtyLsdbPL0ozqEZ92sp7tDY-VcSyOnIWxKotOlwZs71AMEP9LzFQtOwoQ) 。
        *   サービスアカウントに「Workload Identityユーザー」ロール (`roles/iam.workloadIdentityUser`) を付与し、作成したIDプロバイダーからのアクセスを許可します [[30]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGbfIil9Ij24qV8wfLLTA9VVCVZwxwLm_X-D6oPc4upwtoEUcPw6204K66wTP-Ifbn4VokbbcNrDv8SUtCcJoq41dPn71jvoucnH0mSV2CG1pvfYdq6fL7DbdwToAKXBfAppObBoIPJUQJXKUFoew0trAe1sqIPTehIGQrqDf_h5MLTagX67Oh5Pou4w_T) 。
    2.  **HCP Terraform側**:
        *   Workspaceの環境変数に `TFC_GCP_PROVIDER_AUTH` (`true`), `TFC_GCP_WORKLOAD_IDENTITY_PROVIDER`, `TFC_GCP_SERVICE_ACCOUNT_EMAIL` を設定します [[28]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEu1_yacb2RhcG_BDJwfocG9CQTkWG0XfwQgsWmsGrDr6W-ABp-DvhaezlNgX9bBT2TRSFOb2A3AKMEUQv5qBS7ElYjRHC7TxXUfKfuWCXxSH49kIltym3nhk4f9D2tBr5CMtBiptsV8FSPnj0ad8txFNU9BL1dTPVqS-aBIZWUegLNPNwtU4UCfzFPVoSQGSyQ5jb21vnPjYMDcHAOrqFgPJE8J1yX1SqC) 。

#### 3.3. バージョン管理システム（VCS）との連携

1.  Workspace作成時に「Version Control Workflow」を選択します [[25]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCGBrlaF_KsYac3Fk5rhKr-zXAFTD0-jyb0g9GpsAGI58Lwad628O0H0ywrEGcMnP4g7Kj6sx736uyaNVOGb2EA6cJ4IFBtYtHZpY-dykkAZqwSOtO_Aqimw2M1GRqGoPry2NcjWHg-bJcCK0U8hc=) 。
2.  GitHub、GitLabなどのVCSプロバイダーに接続し、Terraformコードが格納されているリポジトリを選択します [[23]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJzB_-DKqAZFFCsPG1Q6v7pzi2wLKcTAYNhEAmvOXDMHWMAy8zmqvqqPf5oyg9iLeV00YidLMXmjLgyXIb6SDalpglorHCnKKIn-WTUuo78HV4OVFyJBArRBIzsCkSC2uNAYmZhMxkkUPAfouaBUMYJb61KrOggbFI)[[32]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2iV_IUj5xO0AUaiPbpvl_Yk88d4zMqzfxSt-6gP5pGcms1FCWm3vLYYZuNf0Zv5iYvpIwaIy5mgRHBGSZjZRVvNpgrMUb8PF_Cc4vCXpDAtgCf3CkRuNWrUyrrrBBPcsEYjM-qDhvbF2li92lAaTxTRLwcPRBZ240r6R0cfsvrwg=)[[33]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIl5gytcDz0Md4dY7T77I5q7638uInjFQ160puRWfaalEjp8IuxP97-lfjHZBNHlom4XL3AukYrzFgG3wOZM9LyS-H-WO3AhAlR77McUTNkQmYZZTmGKB8ATuxcgue3fMUu37sn2yN4ws=) 。
3.  この設定により、指定したブランチへのコードのプッシュをトリガーに、HCP Terraformで自動的に`plan`が実行されるようになります [[34]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1lJi2o-t57o5hct4fHHQHuXHfHogM2AuY6tF5p8A28IbPoSj9LBLkxHshuTF0zqnrK8EbJxVWjlWT8ZoJ1MNOYizRlFuzSfry4e8Y0DvvMgloHFHUuvPmLJTW1L6xvEZXCGcpfw==) 。

### 4. 基本的な利用ワークフロー

#### 4.1. Terraformコードの記述

管理したいGCPリソースをHCL（HashiCorp Configuration Language）で記述します。`terraform`ブロックでHCP Terraformをバックエンドとして使用することを宣言します [[35]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYsE5rYsX99RecalBbDlQbBpJsNeW5pOtaLKv9Gp5vbWGeMnJz4p1aiq9KvnLE8Ckzl64afSmqXvpzOKsff8jGJQ7aMWeV_OAHN_D3V5Pcfgr2892M3iv4HiPmBE-BWCd4DWzFBU7r8ZNUE-Y=) 。

```terraform
# main.tf

terraform {
  # HCP Terraformとの連携設定
  cloud {
    organization = "your-organization-name"
    workspaces {
      name = "gcp-resource-workspace"
    }
  }
  # ...
}

provider "google" {
  project = "your-gcp-project-id"
  # ...
}

# 例: Google Compute EngineのVMインスタンスを作成
resource "google_compute_instance" "default" {
  name         = "terraform-instance"
  machine_type = "e2-medium"
  # ...
}
```

#### 4.2. 実行プランの作成と適用 (Plan & Apply)

VCS連携ワークフローでは、コードの変更がリポジトリにプッシュされると、HCP Terraformが自動的にプロセスを開始します [[36]](https://drive.google.com/a/vorn.co.jp/open?id=1DfR1G8Zj6jPs4zTJOO1rG2irCZzMjDzH) 。

1.  **プランの自動作成 (Plan)**: 新しいコミットがプッシュされると、自動的に`terraform plan`が実行され、変更計画がUI上に表示されます [[34]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1lJi2o-t57o5hct4fHHQHuXHfHogM2AuY6tF5p8A28IbPoSj9LBLkxHshuTF0zqnrK8EbJxVWjlWT8ZoJ1MNOYizRlFuzSfry4e8Y0DvvMgloHFHUuvPmLJTW1L6xvEZXCGcpfw==) 。
2.  **プランの確認と適用 (Apply)**: チームメンバーがプランをレビューし、問題がなければUI上で「Confirm & Apply」をクリックして承認します。承認されると`terraform apply`が実行され、GCP上にリソースが作成・変更されます [[36]](https://drive.google.com/a/vorn.co.jp/open?id=1DfR1G8Zj6jPs4zTJOO1rG2irCZzMjDzH) 。

#### 4.3. Stateファイルのリモート管理

HCP Terraformをバックエンドとして使用すると、Stateファイルの管理が自動化されます [[37]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpHl_2YRdKihJCwmP5SfH4e-Q_I973vKC9UGr4QjhjttQb-uYj4Pb76Rz9YeXWJkI93zU9A8dSZcGAmyLAt9boMogHPZbFFcunzO9BDLuxBK3b5dWbprJT7V0QTYnTSR3lMk5OWqZFshDb4ejizi8g7I-3UWXPY5WB)[[38]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFubBMFCDxJRt5fW680eZ43jdHIJVS2LaRcdNfba3OhRQE2HKSiL1gRPZ3MtdE4mtFHwvX8mcMf1wdz5WiB9llAXPKUT0YvszhocKnMN9wx0LR890aKWQ0dtQKd7vAi0TUiZO7cZiHnGxaopvK3b_zoG98UXgJoHxNi_Afknd5mfQ==) 。

*   **リモート保存**: StateファイルはHCP Terraform上に安全に保存され、チームで共有されます [[38]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFubBMFCDxJRt5fW680eZ43jdHIJVS2LaRcdNfba3OhRQE2HKSiL1gRPZ3MtdE4mtFHwvX8mcMf1wdz5WiB9llAXPKUT0YvszhocKnMN9wx0LR890aKWQ0dtQKd7vAi0TUiZO7cZiHnGxaopvK3b_zoG98UXgJoHxNi_Afknd5mfQ==) 。
*   **状態のロック**: `plan`や`apply`の実行中、Stateファイルは自動的にロックされ、複数人による同時操作を防ぎます [[39]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu_QTBq3sZgQClP4HbyGKgADl9JyUXKqP2slzAEku9SrYsuCE6tFUeACQhQ45Oni2lBF-t4RAsdG0uS9tu-FlZR38CBpnVZUtAXj5pmC8duP627N8FIXzYupYwqoTK56LPsyIqxraX3jXAiNw4tL8=)[[40]](https://drive.google.com/a/vorn.co.jp/open?id=1T6Ey8WkDOHcY-VIuYKZ5x55fhm78JY4i) 。
*   **変更履歴**: Stateファイルの変更履歴もバージョン管理され、追跡が容易になります [[38]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFubBMFCDxJRt5fW680eZ43jdHIJVS2LaRcdNfba3OhRQE2HKSiL1gRPZ3MtdE4mtFHwvX8mcMf1wdz5WiB9llAXPKUT0YvszhocKnMN9wx0LR890aKWQ0dtQKd7vAi0TUiZO7cZiHnGxaopvK3b_zoG98UXgJoHxNi_Afknd5mfQ==) 。

### 5. 大規模組織向けの高度な活用とベストプラクティス

#### 5.1. 組織構造の設計

*   **Workspaceの設計**: 変更の影響範囲を小さく保つため、「コンポーネント（ネットワーク、アプリ等）」と「環境（dev, stg, prod）」でWorkspaceを分割します [[41]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn-5fhjeT0cTU_8sNqTouvoTTbz0YdxsWP7KH_ZwD3QGtgQ8dJgVYOaZOxJU3zpoXw_j9y_KCiR_2l_T5LAaLQId4MFwfV_x8mf97XcH3N3ZjkMm-_5hiDjLOl49d9qjfbrtuKL_YtCyuqlq0yAdc1b0U1tkLAk6Jy_elR68MDOE_Pn8i_k_AV)[[42]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpbslyf5tpX5ncHp4s3pB_WS9kMo19WAFRQE8WYV7P4702PjkCiUOHhPogdWjfnw8Y-2Xp9DZ9XHh2yUSI-AcvEMHhGHCKV2TAOPKjkG_BuoIpK4gkiXVy4r2ig6t1r1or0kZs8tbc7MGLbDSlfORe4OmzWQxZuXVW) 。
*   **Projectの設計**: 関連するWorkspaceをグループ化するために、「事業部」や「チームの所有領域」単位でProjectを設計します [[43]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC_Q_Fx0QsRnXyTIhOgBD2IVIybsswfK2JGXMhuKmLIXWAAf-JYlSQ6VG68kj9FhGbpBXZJg82P95009ZvDLuBokPkgKDN6E3piIoCjmqY7Q0pV4uH0YHp4BU9KWK-62J33MBu4tvjcozIHpYXUSlMiP7rd1pzi4q-kyzzNmS6_WvG9-gEeA==)[[44]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1P-s9VMgIwtJM8RH3MeumsWQTmCtk2YrPsvpstMRAqJ-xU17mFB8NvWuexZDMmOxoSIOpgiYhD2juEv72hPooezcvy57_C351bG3ZzMowdCG3fApLgosEMWs-TPVeeEdNHt2_JyILNRLr_Ly-I5wCXX7wSPRFtHofjY9VglFFc_TU6vTMIJLBi-0Lw4hzG6FLtNNs3kCxLO8Skp6wccjH1ZZJyNYaN0pVksxY) 。Projectレベルの変数セットを活用し、認証情報などを一元管理できます [[43]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC_Q_Fx0QsRnXyTIhOgBD2IVIybsswfK2JGXMhuKmLIXWAAf-JYlSQ6VG68kj9FhGbpBXZJg82P95009ZvDLuBokPkgKDN6E3piIoCjmqY7Q0pV4uH0YHp4BU9KWK-62J33MBu4tvjcozIHpYXUSlMiP7rd1pzi4q-kyzzNmS6_WvG9-gEeA==) 。
*   **Teamとアクセス制御**: ユーザーの役割に基づいてTeam（例: `gcp-network-admins`）を作成し、最小権限の原則に従ってWorkspaceやProjectへの権限を割り当てます [[45]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv0tF5fPjJiItgVeO4dYw_am84p1xjUfEelOGfe5ltLrdb_JvVife4wQuogdUjTLEgwIHEqYoODgpzG1K0vbNdWc94MK5E-Jq1F1Lnrq-gA3JnbDYfS6hU-x_Xe9AdZ7rNx01IwCGb6Z4eEqakzAt-MdTe1I-ZUg==)[[46]](https://drive.google.com/a/vorn.co.jp/open?id=1JsXjYoGP93OfPpyGFRkg4FmI70lxmeqD) 。

#### 5.2. Gitリポジトリ戦略

*   **モノレポ vs マルチレポ**:
    *   **モノレポ（単一リポジトリ）**: 全てのインフラコードを1つのリポジトリで管理します。全体像の把握が容易ですが、大規模になると複雑化します 。
    *   **マルチレポ（複数リポジトリ）**: チームやサービス単位でリポジトリを分割します。所有権が明確になり影響範囲も限定されますが、依存関係の管理が複雑になります [[47]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9jAlhFQ0ia7yuk1xetnyorTW-UOSEZWHU0R5EeGUvxa7YtuhkGZDKsUfL0rxfoQIouQoY-j1HQEBYNWXej5yRViOqWWi-78_fyiztPW4K-XUamR_u-s-_dMLQYVyrCOFOAU5Ywpd2HOvZoyhP)[[48]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6g3Ivvtp_CwhqnCUpgS2Cjd8SYvQugDI5jWNy-BdvmU5Bz8Xu6RB2tPHuyjZtoxzJHRY6v2ZZZf7cNsosfoJlLRorSUTX7IV_hfO9iQgbmyqivxr7nR8qd1NilwaeqxOo6M7VuIxHtlvi2Ne9cg==) 。
    *   多くの大規模組織では、共通モジュールは専用リポジトリで管理し、各プロジェクトの構成は別のリポジトリで管理するハイブリッドアプローチが採用されます。
*   **ディレクトリ構造**: `environments`（環境ごと）と`modules`（再利用可能なコンポーネント）でディレクトリを分割する構成が推奨されます [[47]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9jAlhFQ0ia7yuk1xetnyorTW-UOSEZWHU0R5EeGUvxa7YtuhkGZDKsUfL0rxfoQIouQoY-j1HQEBYNWXej5yRViOqWWi-78_fyiztPW4K-XUamR_u-s-_dMLQYVyrCOFOAU5Ywpd2HOvZoyhP)[[49]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPTM6oPE0f_DB8IO8PIpLyhu8ayZfTBG3gS3qokR3F8-jPriHosNtBholftd_mhjvCuZGRrLncxSOU92V4lnBJ7g-eJ06GzXIz3mN80tQBOMWct55ztfR92Uq4rfscK8EP_S3WHam7xbaUVFQLhcNhgg==)[[50]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHatol1C6OFZXJ9G2wMNbDCQ5NQIbAiC2oMQSgahLec_b6RBh7vrm4tTK-3obmj425k7q7bx6Laadm_iq1UepbFeejbA5-2tjCGIRtDVgHQJtHsLHshJepkzr-jdmrErjPehst8NAdp2-a_XE9PivcmdRylbvbZPtLMbHO-7OhTEME1Jvw_sAj6Eg91) 。
*   **ブランチ戦略**: `main`ブランチを保護し、フィーチャーブランチで開発、プルリクエスト経由でマージするGitFlowベースの戦略が一般的です 。環境ごとにブランチを分ける（`dev`, `stg`, `prod`）戦略も有効です [[51]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIfUbJVOAQQXO6W7M2qPYDW8dEQFRcKTx2M92IzSWq79gryfz_dCuXUBfUSsEnpq5kvhP1aPkKduk7uWh29mx9RNX7x8m07CG9-eZTVs5NO2voDqRHU-lmlalnDQEjjBoHhifaVvIKmeYjtotEPgaC9WoIziyW_8flPvoWN2qOG_TvfZFQWw==) 。

#### 5.3. CI/CDパイプラインの構築

GitHub Actionsと連携し、Pull Request作成時に`plan`を、mainブランチへのマージ時に`apply`を自動実行するパイプラインを構築できます [[52]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRlRzCFhnf37RAy63c-O-R_or1PI_GlCk3uXkICAiTfFQCvku20yI-j_HSMRZKehQG4qMgxlSvmA-Xszx83tNpUnzK6SmVURMtqjwzg2jSiZlPn4KqeOCkOe1_Fp8cqtio4Ac3N17HJpR2FeSRso95NnBQJQsivyt5QSg=)[[53]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPeWILCq2DFHl7bcUeLgTSvy3LAhdZxPr8ZNCRYHpzTYu7qL4Dh1ydvZCUbJPl9saOfEz2ffH2tpKW20_B3r5oNsCLuqpK0JrkjLo5MuxRV0HPWtXXpM9W-q7jZ6XQBl_TqmPFluhpwV95S5ctwccLk1Etx8oSlmkLnziTZYdWPmE64Bdr) 。認証には前述のOIDC連携を利用することで、静的なキーをGitHub Secretsに保存する必要がなくなり、セキュリティが向上します [[52]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRlRzCFhnf37RAy63c-O-R_or1PI_GlCk3uXkICAiTfFQCvku20yI-j_HSMRZKehQG4qMgxlSvmA-Xszx83tNpUnzK6SmVURMtqjwzg2jSiZlPn4KqeOCkOe1_Fp8cqtio4Ac3N17HJpR2FeSRso95NnBQJQsivyt5QSg=)[[54]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGR00wyHhS7-sCVXPWUUEDBdvun7dAMd1kx1Q_PAvcSVkibLOG1x6tB-gPBb2C4hRIfctC-CfcAbr7jCndNB2XOKphnLNcSsV4JXtcS2V_5QX8urvsiqtx2jhO1kGpCQWXdz-USmrJ0GnJadlc=)[[55]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPZUxM-axg8t9GAXOPrUF28E_ufsj-yX3Nxz1z-8e_VHNv4gaSE6umBhqX1B4gBA2-c83ucwa7D9hrT0RWFBJlC6mFvYmy2nS2AhIiJ-lP87jbyJnX21lgcBTy9qLAP_9x-YVhiexYGj1tzw==) 。

**ワークフローの例 (`.github/workflows/terraform.yml`)**:

```yaml
name: 'Terraform CI/CD'
on:
  push:
    branches: [ main ]
  pull_request:
permissions:
  contents: read
  pull-requests: write
  id-token: write # OIDC認証に必要
jobs:
  terraform:
    name: 'Terraform'
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          cli_config_credentials_token: ${{ secrets.TF_API_TOKEN }}
      - name: Authenticate to Google Cloud
        uses: 'google-github-actions/auth@v2'
        with:
          workload_identity_provider: ${{ vars.GCP_WORKLOAD_IDENTITY_PROVIDER }}
          service_account: ${{ vars.GCP_SERVICE_ACCOUNT }}
      - name: Terraform Init
        run: terraform init
      - name: Terraform Plan
        if: github.event_name == 'pull_request'
        run: terraform plan -no-color
      - name: Terraform Apply
        if: github.ref == 'refs/heads/main' && github.event_name == 'push'
        run: terraform apply -auto-approve
```

#### 5.4. ガバナンスとセキュリティ

*   **Policy as Code (Sentinel)** (Standardプラン以上): 「高価なマシンタイプの作成を禁止する」「必須タグの付与を強制する」といったポリシーをコードで定義し、`apply`前に自動チェックできます [[56]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDfFbLOss0VoTpbi4kYSMUrf8A__Ng6O6LQHecfFxZ_JvUbCmxG2iJbr7Vk7c6LE20HrdabWZAk6tAnx659tlhycXTUVdoVaAB-WzuNgKp9ohOeFItF6JBwmdhxx5zfneCw7e_XoaJVtE8hvUJK9UfGgLZykRuMO06oRCI5_QqHQ4ghoHETm2qNBb-ljdGibymKtkVClX6zDlScnD4hM7DWhap8iRusPQ=)[[57]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAmk8-bzHTwSgxfuvIFgkszEsPqA4UwwzlV9LDg5p_vjwPICHLTbts87lUbLwswO4uNfpXU_ygUE7OAOxf1wGv5qjTAgHVub9FywHNopk9qJgXxqLFoTrr7kObuZ4dU9haFV7OZfA=)[[58]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvAUffEq_FsfPu0FQge-iWEdicr_VArU43QHqaC6hmc3HwtcGoW5he21u_bEkom70PL4BIprPn7GDv6mazO8FPqeevV9UK4_7V66JYeL9OkEXIRL8IVfWjkM6jwaDpc76xUYfMNSuC6F0BbdoMHU0vG_AtWJG0Cg==)[[59]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeUFSUWOJzkWXNnnVLSf2ApI1lFUXyqjofucXwWFC-sS-zhbguSmqlEHmDClmEg9_dzzhuyHI1bHl5J-Wc1NuSF6BGW_Ljf-AEThW1MPGO4N2c2PZgIaMw9Bkw2Z_FNZ3LAAFnZi2xBPgLlAb5XG_OMKyOgA==) 。
*   **IAMポリシーのコード管理**: `google_project_iam_policy`, `google_project_iam_binding`, `google_project_iam_member`を適切に使い分け、意図しない権限変更のリスクを最小限に抑えます。特に、個別の権限付与には`iam_member`が最も安全です [[60]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfj6aezRasbW3Dt7n2eQNqKqdaKpRCidEFDA1peAm_FLj1kw2-938Sj18NtytiGEaDKojJT70ps4pU1tFvSvVUCmHoAR523MAvkMaZz-mW5rkGmSfRmL7Dgs_JlfUu0XySMQzO0PrtHOde1KCD0e52KVx0RhsILzEJnq7gWQbV9NeRD9fgu1sk)[[61]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHu3F8OPCLx3ed907METqpE2QF2RRN3CCIxrOykXU6csWeYZ5JKDzXpyar4wi9cr6YHRsDYa4FRBKJLzm15iYQdXSqY-a2wffpDpdvrnkL_R313m1s1y70vO3hZU9MeC6Zh64lOJFETvivQZvPrIoaJcdNX9kbj4MASBy5X)[[62]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC1h5YbgzqGZwrWreRug8HakP12tX8aNpnzWJctfcOOOBLxztGa7A74SwRHhnwFBGTnpAfuvM7llQAj3zdQOCoXWIjoLy3F7OB-DCSCk9i6KiMhG2hygo2bSgdvmw-fh-6nvZcsHrIr4mkoBSwbjjZT7rWGPMWcP_JOKrF5GVa8efN3lwon17STk8nN86w2chnQ0gQXdWh) 。
*   **Drift Detection** (Plusプラン以上): Terraformの管理外で行われた手動変更（ドリフト）を定期的に検出し、通知する機能です [[63]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdDo2LFX3ZIb44g6NRP1meNcFqi0d6DEY2K8w_yh3pQd6GmO4S7oFl3rNPFdg8S_tE2GKc-9gNMviW7auR9Rh6eED6MDQWikcz6U779ZsCMxNVSX6t9CNQ7W6MsGDJVid_jywvEEb5k9eoTTYrfLSkK0_GMOFlSwWYdquiyZnwvFYvgmE=)[[64]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhe_h2crVre5Isauh4C13bti4q4Am-Ir_eq8UVd7Nvl3QyLRnJjdYlbKlu4n76sY_UzY_jBSDAvD627uKhj7s47WCnGe54URyfUf9mzmdtjbxqOeSgHxHym8pPsg7CYW1eJHmV3VNNSS2RRgigdeKhpkx7GLdqRGje908gAvxplpBAWmSYzNSVD99CRw==)[[65]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzw8fUIKgBTSbI-bHsrS38e63JAApYmkiRhrY34owyIsQWVS5AIKGf9eJE09-qGa0zSDlNXwr0Qhw9RLSMbQ_h4ZNrkJbBfLAXTmN0Ug4mkddTgIHUhxcJMoCghaiod5QMoA==) 。ドリフトが検出されると、Slackやメールに通知を送ることができます [[66]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPMD_x8XBrkH-WT3VfrWv1u3tZ8ATBk2zdmI8-PZGRRnj22ZGpZqzVRSctWtlG_kVdFUOJZ-UDgojUqQUTXZuNBWRmZQWa1W9tTJdVUK6XTsSnN_Ln1npGjzeN-UkG2gAAmQ13tATQF0DjZhGPB6NR2vMmlBEIzjWV6ACz55cvove8Kc2Owy6sBW0K9jtVag==)[[67]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0yX3AOzlcNyDzoKBdd5ftkwDXfjaOADne72tukgwC7gtjwXuQgGPzkXzcolvzTZaSYsEZ7yMVZSvs7tRe-AcnIQCQ3rnaqskZcgOVvAHuikQ89hcHnizGtAVaoYTntCT9dKE3AAfXsbutFpRFZn8Ljeg4f-BCr-4zOdnWq7i6Rm40HqvdUJXMzHCud5ejpwhx) 。

#### 5.5. プライベート環境との連携 (Agent)

HCP Terraform Agent (Plusプラン以上) をプライベートVPC内にデプロイすることで、外部IPを持たないGKE限定公開クラスタやCloud SQLインスタンスなど、インターネットから直接アクセスできないリソースも安全に管理できます [[68]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQ9A2D9-qZk2yyyv-InVzqwu9YIj_9BCei7ckStNsFV5KUJxCls28nyZRlpOsfNvg9hLVISV3VI3jvohoeS0robrXemxRwoAnD2Zu5me-a0S_jbTcig0kPv-WEB2JoKp-liGmfkDEmnWiSA_FvmteLtdC8WSPgYU547krZY4q68vanSZifEsgcRm2wKv_ViOPHEoWorAW9EUrRVwYwLoVwDW0T5wCiEE8tUEH2X4Ww_p8XmOzTGBW_I1KH5pFjHGxUeprk_ZxsHWl-YbqjxhbU0Zo=)[[69]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9aYBddcDDqtUjQbmQnNMLxJZFfe5adVargskf2TgMHok7gPwrmTaiwgC65tJBllkSSmrq4fs31q_8moSV1bUFxGWeGbUTfBUWJXJSaEtqeWRrYF4vl-W16qZpaT7BHRa_ZzQTP9Q=)[[70]](https://drive.google.com/a/vorn.co.jp/open?id=1Id_-USEUAqOR_KuXzcCbenpJaMwQtOHi)[[71]](https://drive.google.com/a/vorn.co.jp/open?id=1EMhd4DDxvPbxoM9VZ96EceI6iTc4RAsp) 。

#### 5.6. 複雑な構成の管理 (Stacks)

Terraform Stacks機能を使うと、VPC、GKE、データベースといった複数のインフラコンポーネントを一つの単位（スタック）としてグループ化し、宣言的に管理できます [[71]](https://drive.google.com/a/vorn.co.jp/open?id=1EMhd4DDxvPbxoM9VZ96EceI6iTc4RAsp)[[72]](https://drive.google.com/a/vorn.co.jp/open?id=1DPL5pRQo0FvCUCF_jruOfXaO8AZMgQJs)[[73]](https://drive.google.com/a/vorn.co.jp/open?id=1DtK3AJFdw5zZyKffrzDrfXOqFJmKl1jI) 。これにより、マイクロサービスアーキテクチャのような複雑な環境のプロビジョニングを簡素化できます [[74]](https://drive.google.com/a/vorn.co.jp/open?id=1n5bTRBoEnnHjkL1IwVy8iTuXRvgLp3Tb) 。

### 6. コスト管理

#### 6.1. RUM料金体系の概要

HCP Terraformの料金は、主に「管理下のリソース数（Resources under Management - RUM）」に基づいて計算されます [[75]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwpxlqvOyJf7iCLU-nOmugo5qfnN8crJYLmj6DWjA4i2muipptOREPGsHSrV_ESy3Rsrl7Py0xkdq8UPZ5JU4UORdFQrOa1efSYGCmdADI6m0piTZnV7bagUW368DtyCNixv-YVnohoAhmJa4iqUb3PZWDUonY4zU-QSZhn8lS5K39sL6CB_3LZoWWNFT_fAk1_O4=)[[76]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVToml6DbzpObzh-cW5_jJI7EjRlWzKWtLiXQrmsGD1mU-9t3lfvojKLR4cXRjOvFdXtPVBhcE-kHvwkf8tiClz9NHhQVR1erLlWL0D1OM90YMDIamknjvgCGkMONZelaRV_MqsXw6DqUIR_l0K7exyozMZRS8KeVzdOdhKpFmRmuBIws=) 。これは、TerraformのStateファイル内で管理されているリソースの数を1時間単位で集計するモデルです [[75]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwpxlqvOyJf7iCLU-nOmugo5qfnN8crJYLmj6DWjA4i2muipptOREPGsHSrV_ESy3Rsrl7Py0xkdq8UPZ5JU4UORdFQrOa1efSYGCmdADI6m0piTZnV7bagUW368DtyCNixv-YVnohoAhmJa4iqUb3PZWDUonY4zU-QSZhn8lS5K39sL6CB_3LZoWWNFT_fAk1_O4=)[[77]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzVi_5K1PcZoJGHx6F9PXFRNPylbzBdAoSXxOubsMJsVHKNtod2a7xjg-DKBq5ykbJQ3r20Nrq61ZkDYXgHl1LHIXDxCSo55_5Rmre2SOxGgXKDaoVDqv0J7AeJIzn-vRh61EQN82B9dHnfJP8FJT9f88fYc7PLORkaN8pmVJkN7GF_eFu6jptDOUIcDo6eL5vXRVoha-c1ZW0ZN48DTjMLc7xqYe2D2999xPX84qX0ePnlgJXtlE=)[[78]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWp_1vyhmj2SJGn6SYU09Y4BWJsTcfaLbwTMrHVA476lqlvLI-_SHDFp4LFHLp2jQ2f4-5MipM14dOAuVZnuoIpxREvU0Y2XBZGB3Uw78vxUXCdcI7-Zj82QCMBN54AhiTf44j-JCsD3eiFf7UpNPZwo6mc1rY1CxhBZ99) 。各プランの詳細な機能については、セクション2.4をご参照ください。

#### 6.2. コストの予測・監視・最適化

*   **予測**: HCP Terraform標準の**Cost Estimation機能** (Standardプラン以上) や、オープンソースの**Infracost**ツールをCI/CDに組み込むことで、`apply`前にコストへの影響をレビューできます [[79]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-pSoGeZ4Bs93MkcwBZRCGIKNXE8Z_4jhzhmphftupOwAbWYD5qVhjlhsRK0l8lvhuIzDigJVrcQRGQE6AguGyh8Zu1MJMyDMiUAuwLMvGl2GeAJbHaEUPLK5kyFSP6BOKIfQqKtdqTFHi8M-yIbL1j_zKSI58WMoilTvgh9Q=)[[80]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq4lM7evESIk_BGpCDl_FAZX0zPApBzO25s9ggHvcKTWVUXDh-dfxZNOCobga8SGHWL1DNVf2QzI_TDYH1vQy_JAvRUFhKQ2rpYRQmRO_4sgwUe8lP23OMtZkbxzhVGU9xcRch0nautR2cMavhNtWPmi_SFBkNGVFhh3uJYStP7LaxW-IWKw==)[[81]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzLUuC5THkbHlXvErgbZhNjPksO_ufQDoFUVuRIo2YybtEKNcQShOP3IDN0uaYZq70Inrph92VA2Agn_atr9uQWxt8RF9YI_Z419TOc0PLTFLrkajVsFxAG_maFTvu4k2QrI8DYZTrivcp) 。
*   **監視**: HCP TerraformのUIダッシュボードやAPIを利用して、現在のリソース数や概算コストを継続的に監視します [[82]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9Gpqc2f0X5G6eY3_BO1O8OLBt6WrPcbH8mV1QdsbwGs1Pn8bKGs-ylv_o90S0fToY3-0Fr8lm0nRl3x8zqJ7rg6jV7KO-lumKSInlnw1ON3QKesvRGohhb8eQVGe-yeQ212xmKgiB7Fh0VlzXdgHcmv4mtsUTzNOTlxckj8hd8brKkJWVA4xi)[[83]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4zmn3g60mjs_HEpS4fqnP5GOG9YrPtEBz2TP98DnBZvQQ1CUW-UUf5A_1OAqsJyce8PTGjQDH-KQpMduh1IYh0vM97pCVV42Dfua-JPgdeV2FHkcTM7Zh2C2x23n6JSv3c2sL1io-exM=) 。
*   **最適化**:
    *   **アイドル状態のWorkspaceの整理**: 使用していない開発環境などのWorkspaceを定期的にアーカイブまたは削除し、課金対象リソースを減らします [[84]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwtmA72hi-IRJdwyHOm-UoIVHt_yRgWpn8yIq7sNEewpHAG8W-MGD5XqFoM5Yb1ymce4tRif7PMWKpZFh172G3lP6Aue7viyUaag6mCoX6dSDyd16irvLWDr2Lev23e_TUwhY=) 。
    *   **ポリシーによる統制**: Sentinel (Standardプラン以上) を使い、高価なリソースの作成を禁止したり、コスト増分がしきい値を超える変更をブロックしたりします [[85]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeWiSFp-GrJ7GMlZlHbBA83AmNfDcpdhMKzVUeqWexECejPMY2qjvXl-arZI260s2W1eSyzWYM-yJPT-fcCG3A1ft3o1iQUmdMFmye2tfewYTm68PKcptjvEk2IrUVgl1-1LRlNn5x98j7WidLLQVimogeVTUKV2XamOlvxseJ_6RdYQ5HORT92SMAZhtK2TFrUw6RLO7Y3GJYbiIsfxjDU_xw5JA64bIo0cSbKV8=)[[86]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeejP0q16eW5Et2SkQWSe3xoE0s4COE_dYoME3djlEmqJ9abNo21ml6gJm348jVklVXzucvpmBhNANIMqxdPFqRb5cd3W2UQeR2zUgNR65ThM-OAciYgd3KTRdITuFSJAspZU3JbFuHxOhQM-uPB8bbpjz0lnWo0JBem5Jmb3RWZnXzu9H)[[79]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-pSoGeZ4Bs93MkcwBZRCGIKNXE8Z_4jhzhmphftupOwAbWYD5qVhjlhsRK0l8lvhuIzDigJVrcQRGQE6AguGyh8Zu1MJMyDMiUAuwLMvGl2GeAJbHaEUPLK5kyFSP6BOKIfQqKtdqTFHi8M-yIbL1j_zKSI58WMoilTvgh9Q=) 。
    *   **標準化されたモジュールの利用**: コスト効率の良い構成をモジュール化（"Golden Modules"）し、組織全体で利用を推進します [[87]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvOw-qFbX562mrQZuO5kDG4mXNJZsICgEqrmG8AhZkgoWa7snhyiYyYZgg1SIrVKcLPF9s-8jXpXwrhJRSB0CUH0Sop3tB4TQeL7TTyTSWqJykwNFotfJcOIAuJ6wLEOMs1OUBxMY942eoE7-kr7dMIlqIFcu43244hTlIKkuWjxYRDgQL_CUk5Q==)[[80]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFq4lM7evESIk_BGpCDl_FAZX0zPApBzO25s9ggHvcKTWVUXDh-dfxZNOCobga8SGHWL1DNVf2QzI_TDYH1vQy_JAvRUFhKQ2rpYRQmRO_4sgwUe8lP23OMtZkbxzhVGU9xcRch0nautR2cMavhNtWPmi_SFBkNGVFhh3uJYStP7LaxW-IWKw==) 。

### 7. 既存環境からの移行

オープンソース版TerraformからHCP Terraformへの移行は、簡単な手順で実行できます。

1.  **Stateファイルのインポート**:
    *   ローカルのTerraformコードにHCP Terraform用の`cloud`ブロックを追加します 。
    *   ターミナルで`terraform login`を実行してHCP Terraformにログインします [[88]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjSZO-M_H9y0jJMhpQd4E4AH5-zTDpwpJxAdLurgnIY5bm4iORWaOgGmOGQrUajjLwrT2Yx6XUv-RxyJ_hWxP6t2QnhTLOGVQ1MoPWu9_2iI06IFV5grBM51skEtzJLu5BfFiHyVIJf5DURs4vKQ==) 。
    *   `terraform init`を実行すると、既存のStateファイルを新しいバックエンド（HCP Terraform）にコピーするか尋ねられるので、`yes`と入力します [[89]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEO3ox51Iq27oy-teBHPffnVPc4q8lpXnI3qwPSxiriWjI9zgXfzLMAbEs-9yVfJ_eQ-P2Hfe6zjCgyrS98XlmZWBQF1dDLHYFVTAEbBYdYcCR3D1rPQUryK5EH3RwpKOpbXWGS1xk7IjL78FiyPpVN_vIYckb3Vn3TP47G-EwLvi7f)[[88]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjSZO-M_H9y0jJMhpQd4E4AH5-zTDpwpJxAdLurgnIY5bm4iORWaOgGmOGQrUajjLwrT2Yx6XUv-RxyJ_hWxP6t2QnhTLOGVQ1MoPWu9_2iI06IFV5grBM51skEtzJLu5BfFiHyVIJf5DURs4vKQ==) 。
2.  **安全な移行のためのベストプラクティス**:
    *   作業前に必ずStateファイルのバックアップを取得します。
    *   本番環境の前に、小規模な開発環境で移行手順をテストします。
    *   APIキーなどの機密情報は、HCP TerraformのWorkspace変数（Sensitive設定）に移行します [[90]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgGTVDXw5032jzDa28sDed95QZJgjE-IwoVfgYG4exVGwjtepKhIJETfk9x3C-ZntH4STc6Bhj8xQfH02f2VVUBDoDcbocQzN5qCIk82SorIWIbpKARBz5UNLxgmMfveQEv_tGiTTPBcdF0qKAvmw=) 。

### 8. HCP Terraform vs Terraform Enterprise

大規模組織では、SaaS版であるHCP Terraformと、セルフホスト版であるTerraform Enterpriseのどちらを選択するかを検討する必要があります。

| 観点 | HCP Terraform (SaaS版) | Terraform Enterprise (セルフホスト版) |
| :--- | :--- | :--- |
| **概要** | HashiCorpが管理するSaaS [[91]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGz2vbg8s9yHmezKlee-KpP8MNnVhw34uYECCM6ATMu2W6zufpPlFq-c0hsiFca_paHiDjziH8U0zndexrikvAsKk1O4OmiddpVucR1otEHwzYRRblTxexzXGppaxRRzqQ3JI-N)[[92]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX5tdPkCXWNjPTr1wcmFDFVuTaEoOsI7i8Em21HWIHhm3ZpPvr9fh9kOjqeAafzdqFZW623aIbGuL6ghluSxcv7r_QuOEHaj4E3rylGSPhYCWjrUFG0Xn6KxlndrxflaidgEJDvP14n2-GdtC0CzUbj3eGawVCNEdIvfzY)  | ユーザーが自社インフラに構築するセルフホスト版 [[93]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGytE26uIUzOJI7noHKYYU2umGIjqJYy83PLOpi6A3h2qrFCsmbOD5zTdtIHjiM9iM4Ix3vc5NlY4i4_QfX-hgsprEFEkTPxjY3xmZv4QF6X0_UGaJ4lg0D2tQc7IlxlcHbuwCH0UbO208=)[[92]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX5tdPkCXWNjPTr1wcmFDFVuTaEoOsI7i8Em21HWIHhm3ZpPvr9fh9kOjqeAafzdqFZW623aIbGuL6ghluSxcv7r_QuOEHaj4E3rylGSPhYCWjrUFG0Xn6KxlndrxflaidgEJDvP14n2-GdtC0CzUbj3eGawVCNEdIvfzY)  |
| **メリット** | ・迅速な導入、低い運用負荷 [[94]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMBED1TKEflkGQxGkHT7mcnTkJ9ni1C42NlBgrg8qeZhqZPREua-EEVmLFgk0d9hv77sfpmeLCObJ_Ewl2Ceh4T0z_d7-e-1LZlv59PupTSZ_xPqacS2yarYr2UESBoN688U2dbVoIS8Av_4nxL2xyIDgf) <br>・初期投資が不要 <br>・常に最新機能を利用可能 [[91]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGz2vbg8s9yHmezKlee-KpP8MNnVhw34uYECCM6ATMu2W6zufpPlFq-c0hsiFca_paHiDjziH8U0zndexrikvAsKk1O4OmiddpVucR1otEHwzYRRblTxexzXGppaxRRzqQ3JI-N)  | ・データを外部に出さず、厳しいセキュリティ要件に対応可能 [[95]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRTGzPDYxK0bwqGQKhnRP9D-WLu2Q5hj4XzGjcIXTnzpvTVJIpolk0XKoXdtfuXBIUeTYwBiz2phojP2rz1gFN85jm3mpUiLS4pQ7r0odryOGDA1hq4iJaL6CQO84ey6i3ox7r6nf8n66QfD7TVi-knh-w7mZEcar_k5lGdIuV-rf92-Nvs5RRWAUDdWW_H6wDKo5ofx1nmgPCinScDcMyioKUMycBaz8qDmJg)[[96]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFETUZtlain9IunwvaT7er7PdjT8mB3KZ5Q8D-kCrpWtyrMBPYcexWpX19wnhfr-Wsl5l8385V0YeXA1PQE014LjRm387lKFpyDZbKactzCOVM7NK62ZrSbGaooiirkAyd2wcbGlIyIyx8rkpTER6ugRs8YJ7s06d3lw4mbNQ==) <br>・エアギャップ環境でも利用可能 [[97]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTR3-ATCK1BptEHtNEh1T_J40y1GqfuN87FD30t8WYOkEdhQu91b1opvGMZCEc7rND58KMsOnBtcIVtNXvgAem_giWoU50ITtJunYfguLPery5mDnB_bbH_PxmHVCW6oJyhllT3NQxz2yYQXA1He1Ek9XTfxhw-ZucZxhSa5LCGDqsHi1ylculAoYJoM7RSCsHWU9O_U5bjwmYJNpLFywQvB9iTqPcxKtJS0AqwsXXkhyHF8zffxraMgy5kiGcuIV78XeqDRSvt870tP71CLpTu3FikTle-Acir9-qjF_cIs-4cTegGLj3qIO_yCygrvdYWgFVnWKtngb0ZgxZBwhyHG93cJMO) <br>・インフラの完全なコントロール [[95]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRTGzPDYxK0bwqGQKhnRP9D-WLu2Q5hj4XzGjcIXTnzpvTVJIpolk0XKoXdtfuXBIUeTYwBiz2phojP2rz1gFN85jm3mpUiLS4pQ7r0odryOGDA1hq4iJaL6CQO84ey6i3ox7r6nf8n66QfD7TVi-knh-w7mZEcar_k5lGdIuV-rf92-Nvs5RRWAUDdWW_H6wDKo5ofx1nmgPCinScDcMyioKUMycBaz8qDmJg)  |
| **デメリット** | ・データを社外に保管する必要がある [[91]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGz2vbg8s9yHmezKlee-KpP8MNnVhw34uYECCM6ATMu2W6zufpPlFq-c0hsiFca_paHiDjziH8U0zndexrikvAsKk1O4OmiddpVucR1otEHwzYRRblTxexzXGppaxRRzqQ3JI-N) <br>・エアギャップ環境では利用不可 | ・構築・運用に高いコストと専門知識が必要 [[97]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTR3-ATCK1BptEHtNEh1T_J40y1GqfuN87FD30t8WYOkEdhQu91b1opvGMZCEc7rND58KMsOnBtcIVtNXvgAem_giWoU50ITtJunYfguLPery5mDnB_bbH_PxmHVCW6oJyhllT3NQxz2yYQXA1He1Ek9XTfxhw-ZucZxhSa5LCGDqsHi1ylculAoYJoM7RSCsHWU9O_U5bjwmYJNpLFywQvB9iTqPcxKtJS0AqwsXXkhyHF8zffxraMgy5kiGcuIV78XeqDRSvt870tP71CLpTu3FikTle-Acir9-qjF_cIs-4cTegGLj3qIO_yCygrvdYWgFVnWKtngb0ZgxZBwhyHG93cJMO)[[98]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdim9Wi2QZc2INtvIV3S3CgbA97lMZpopSTYchJVznLPqPZ4D2EqQJ-znaD60_zgLYjnq0cmXauzbZ2RdfFLr0dDMyKoXiVoRlQspk3_7zTTXDUeQSkIt87u1J2v6XiZebFsghE9A=) <br>・アップグレード作業は自社で実施 [[97]](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTR3-ATCK1BptEHtNEh1T_J40y1GqfuN87FD30t8WYOkEdhQu91b1opvGMZCEc7rND58KMsOnBtcIVtNXvgAem_giWoU50ITtJunYfguLPery5mDnB_bbH_PxmHVCW6oJyhllT3NQxz2yYQXA1He1Ek9XTfxhw-ZucZxhSa5LCGDqsHi1ylculAoYJoM7RSCsHWU9O_U5bjwmYJNpLFywQvB9iTqPcxKtJS0AqwsXXkhyHF8zffxraMgy5kiGcuIV78XeqDRSvt870tP71CLpTu3FikTle-Acir9-qjF_cIs-4cTegGLj3qIO_yCygrvdYWgFVnWKtngb0ZgxZBwhyHG93cJMO)  |

**選択基準**:
*   **HCP Terraformが適しているケース**: 迅速な導入と運用負荷の低減を重視し、パブリッククラウド中心の開発を行う多くの組織。
*   **Terraform Enterpriseが適しているケース**: 金融・政府機関など、データを外部に持ち出せない厳しいセキュリティ・コンプライアンス要件を持つ、またはエアギャップ環境での運用が必須の組織。

### 9. エグゼクティブサマリー

HCP Terraformは、Google Cloudをはじめとするクラウドインフラの管理を、コードに基づいた安全で効率的なワークフローへと変革する強力なプラットフォームです。

導入を成功させるためには、以下のステップを踏むことが重要です。

1.  **基本とプランを理解し、準備を進める**: HCP Terraformの機能、メリット、そして自社の要件に合った料金プランを理解し、OIDC連携によるセキュアな認証設定を含む、Google Cloudとの連携準備を確実に行います。
2.  **CI/CDを構築する**: GitHub Actionsなどのツールと連携し、コードのレビューからデプロイまでを自動化するパイプラインを構築します。
3.  **組織規模に応じた設計を行う**: Workspace、Project、Team、Gitリポジトリの構成を戦略的に設計し、ガバナンスと効率性を両立させます。
4.  **高度な機能を活用する**: Policy as Code (Sentinel)、Drift Detection、Agentなど、選択したプランで利用可能な高度な機能を活用し、セキュリティと運用レベルを向上させます。
5.  **コストを管理する**: RUM料金体系を理解し、コストの予測・監視・最適化の仕組みを導入します。

多くの組織にとっては、運用負荷が低く迅速に導入できる**HCP Terraform (SaaS版)**が最適な選択肢となります。一方で、非常に厳しいセキュリティ要件を持つ場合は、**Terraform Enterprise (セルフホスト版)**が唯一の選択肢となることもあります。
